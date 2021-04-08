# IMPORT DEPENDENCIES
import os
import pandas as pd
from psychopy import core, event, gui
from random import shuffle
from time import strftime

# COLLECT USER/EXPERIMENT INFO
def prompt():

    myDlg = gui.Dlg(title = 'exc')
    myDlg.addText('Subject Info')
    myDlg.addField('ID:')
    myDlg.addField('Condition:', choices=range(3))
    myDlg.show()
    
    # quit if participant does not click 'ok' or pnum blank
    if not myDlg.OK or str(myDlg.data[0]) == '':
        core.quit()
    else:
        pnum = str(myDlg.data[0])
        cnd = myDlg.data[1]

        data = pd.DataFrame(columns=['pnum','condition','phase','block','trial','category1','category2','item1','item2','response','latency']) 

    return [data, pnum, int(cnd)]

# SAVE DATA TO CSV
def save_data(data, subject_dir, pnum, cnd):

    time_stamp = strftime('%Y-%m-%d')
    filename = os.path.join(subject_dir,'exc_{}_{}_{}.csv'.format(str(cnd), pnum, time_stamp))

    while os.path.exists(filename) == True:
        filename = filename[:-4]
        filename += '_dupe.csv'

    data.to_csv(filename,index=False)
    
# INSTRUCTIONS, WAIT FOR BUTTON PRESS TO ADVANCE
def transition(win, instructions, phase, class_map):
    
    SR1 = 'Thank you for participating in the following experiment.\n\nIn this section, you will be shown pairs of squares that vary in their size and shading. Your task will be to evaluate how visually similar the two squares are using a slider on a provided rating scale. It is important that you factor both shading and size into your decision. \n\nTo use the scale, simply click the mouse over the point on the scale that you feel is most appropriate given the present pairing. There are no numbers on the scale, so just use your best judgment when evaluating similarity, and don\'t hesitate to use the end points of the scale when necessary. \n\nWhen you are ready to get started, please press the SPACEBAR.'
    
    classify =  'In this next section, you will be shown the same squares as before. The examples now belong to two different kinds and your job is to learn to tell which ones are from which category: {}s and {}s.\n\nAs you are shown each example, you will be asked to decide its category. To make a selection, simply click on either category name. You will receive feedback on each trial to help you learn. At first you will just have to guess, but you will gain experience as you go. It may not be easy, but before long, you should develop a good sense of the two categories.\n\nWhen you are ready to get started, please press the SPACEBAR.'.format(class_map['A'], class_map['B'])

    SR2 = 'In this next section, your task is to rate the similarity of the square pairings once again. The task is identical to the first section of this experiment.\n\nWhen you are ready to get started, please press the SPACEBAR.'

    CONF = 'In this next section, you will be presented with examples of the {} and {} classes individually. Your task will be to categorize each item using a scale.\n\nTo categorize an item as an {}, click on the slider left of the center point; to categorize as a {}, click it right of center. How far you select a point away from center indicates how confident you are in your categorization (on a scale of 1-100% confident); further towards the left or right side means you are more confident; closer to the center means you are less confident.\n\nWhen you are ready to get started, please press the SPACEBAR.'.format(class_map['A'], class_map['B'], class_map['A'], class_map['B'])
    
    goodbye = 'You\'ve reached the end of this experiment. Thank you for your participation.\n\nWhen you are ready, please press the SPACEBAR to close this program. Be sure to notify the experimenter that you have concluded this study.'

    text_map = {'sim_rate_1':SR1,
                'classification':classify,
                'sim_rate_2':SR2,
                'conf_rate':CONF,
                'end':goodbye}

    instructions.setPos([0, 0])
    instructions.setText(text_map[phase])
    instructions.draw()
    win.flip()

    resume=event.waitKeys(keyList=['space', 'escape'])
    if resume[0][0]=='escape':
        win.close()
        core.quit()

# DRAW TRIALS: LEARNING PHASE
def classify(win, img, text, button_boxes, button_labels, class_map, cursor):

    text_labels = button_labels[:] # make copy that can be shuffled

    if button_labels[0] == '{}'.format(class_map['A']):
        abscissa = [-250, 250]
    else:
        abscissa = [250, -250]

    shuffle(text_labels)
    
    img.setPos([0, 20])
    img.draw()

    text.setPos([0, 375])
    text.setText('Is the following square a(n) {} or {}?'.format(*text_labels))
    text.draw()

    for options in range(len(button_labels)):
        button_boxes[options].setPos([abscissa[options], -350])
        button_boxes[options].draw()
        text.setText(button_labels[options])
        text.setPos([abscissa[options], -350])
        text.draw()
   
    win.flip()

    pressed=False
    
    timer = core.Clock()

    while pressed==False:

        text.setPos([0, -350])
        
        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
            
        elif cursor.isPressedIn(button_boxes[0], buttons=[0,1]):
            
            result=1

            text.setText('Correct! This square is a(n) {}.'.format(button_labels[0]))
            text.draw()
            img.draw()
            win.flip()
            core.wait(2)

            pressed=True
        
        elif cursor.isPressedIn(button_boxes[1], buttons=[0,1]):
            
            result=0

            text.setText('Incorrect! This square is a(n) {}.'.format(button_labels[0]))
            text.draw()
            img.draw()
            win.flip()
            core.wait(2)

            pressed=True
    
    latency = timer.getTime()

    return [result, latency]

# DRAW TRIALS: SIMILARITY RATING PHASE
def rating_similarity(win, left, right, img, text, scale, cursor):

    scale.reset()
    
    text.setText('Using the scale below, please rate how similar the two on-screen squares appear to be.')
    text.setPos([0, 400])

    while scale.noResponse:

        abscissa = [-300, 300]
    
        for n_img in [left, right]:
            img.setImage(n_img)
            img.setPos([abscissa.pop(0), 20])
            img.draw()
        
        text.draw()
        scale.draw()
        win.flip()

        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
    
    win.flip()
    core.wait(0.5)
        
    return [scale.getRating(), scale.getRT()]

# DRAW TRIALS: CONFIDENCE RATING PHASE
def rating_confidence(win, img, text, scale, cursor):

    scale.reset()
    
    text.setText('Using the scale below, click a point to select the correct category and your confidence.')
    text.setPos([0, 375])

    img.setPos([0, 20])

    undecided = True
    
    while scale.noResponse and undecided:

        scale.draw()
        text.draw()
        img.draw()
        win.flip()

        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()

        elif scale.noResponse == False:
            rating = scale.getRating()
            if rating != 0:
                undecided = False
            else:
                text.setText('It looks like you didn\'t choose either category. Please give your best guess and submit again!')
                text.draw()
                win.flip()
                core.wait(2)
                text.setText('Using the scale below, click a point to select the correct category and your confidence.')
                scale.noResponse = True
                
    win.flip()
    core.wait(0.5)
    

    return [rating, scale.getRT()]
    
