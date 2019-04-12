# IMPORT DEPENDENCIES
from psychopy import gui, core, event
import os
import pandas as pd
import random as rnd
from time import strftime

# COLLECT USER/EXPERIMENT METADATA
def prompt():

    myDlg = gui.Dlg(title = 'SELF')
    myDlg.addText('Subject Info')
    myDlg.addField('ID:')
    myDlg.addField('Condition:', choices=[1,2])
    myDlg.show()
    
    # quit if participant does not click 'ok' or pnum blank
    if not myDlg.OK or str(myDlg.data[0]) == '':
        core.quit()
    else:
        pnum = str(myDlg.data[0])
        cnd = int(myDlg.data[1])

        data = pd.DataFrame(columns=['pnum','condition','phase','block','trial','category','item','result']) 

        return [data, pnum, cnd]

# SAVE DATA TO CSV
def save_data(data, subject_dir, pnum, cnd):

    time_stamp = strftime('%Y-%m-%d')
    filename = os.path.join(subject_dir,'SELF_{}_{}_{}.csv'.format(str(cnd), pnum, time_stamp))

    while os.path.exists(filename) == True:
        filename[:-4] += '_dupe.csv'

    data.to_csv(filename,index=False)
    
# SPLASH SCREEN WITH TEXT, WAIT FOR BUTTON PRESS TO ADVANCE
def transition(win, instructions, data):

    hello = 'Thank you for participating in today\'s experiments.\n\nIn your first task, you will be shown examples of two kinds of alien creatures. The examples belong to two different kinds, and your job is to learn to tell which ones are from which category: MAKMAKs and SWIBs.\n\nAs you are shown each example, you will be asked to decide its category. You will receive feedback on each trial to help you learn. At first you will just have to guess, but you will gain experience as you go. It may not be easy, but before long, you should develop a good sense of the two categories.\n\nWhen you are ready to get started, please press the SPACEBAR.'

    test = 'For this next task, you will be provided with a category label (MAKMAK or SWIB) and asked to choose which of two on-screen examples is the better example of the provided category. All but two parts of the examples will be hidden from view. The visible parts will differ between the two examples. To do well on this task, you will need to use your knowledge of which parts go together for a given category label.\n\nWhen you are ready to get started, please press the SPACEBAR.'
    
    goodbye = 'You\'ve reached the end of this experiment. Thank you for your participation.\n\nWhen you are ready, please press the SPACEBAR to close this program. Be sure to notify the experimenter that you have concluded this study.'

    instructions.setPos([0, 100])

    if len(data) == 0:
        instructions.setText(hello)
    elif len(data) < 65:
        instructions.setText(test)
    else:
        instructions.setText(goodbye)

    instructions.draw()
    win.flip()

    resume = event.waitKeys(keyList=['space', 'escape'])
    if resume[0][0] == 'escape':
        win.close()
        core.quit()

# DRAW RELAVENT VARIABLES TO SCREEN
def draw_all(win, category, image, instructions, boxes, labels, cursor):

    pressed = False
    event.clearEvents()
    cursor.clickReset()
    
    instructions.setPos([0, 275])
    instructions.setText('Is the following alien a MAKMAK or SWIB?')
    instructions.draw()

    xcord = [-250, 250]
    rnd.shuffle(xcord)

    for i in range(len(boxes)):
        boxes[i].setPos([xcord[i], -300])
        boxes[i].draw()
        labels[i].setPos([xcord[i], -300])
        labels[i].draw()

    image.setPos([0, 0])
    image.draw()
   
    win.flip()

    while pressed == False:
        
        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
            
        elif cursor.isPressedIn(boxes[0], buttons=[0,1,2]):
            
            result = 1

            instructions.setText('Correct! This alien is a {}.'.format(category))
            instructions.draw()
            image.draw()
            win.flip()
            core.wait(3)
            pressed = True
        
        elif cursor.isPressedIn(boxes[1], buttons=[0,1,2]):
            
            result = 0

            instructions.setText('That is incorrect. This alien is a {}.'.format(category))
            instructions.draw()
            image.draw()
            win.flip()
            core.wait(3)
            pressed = True

    return result

## VERSION OF DRAW ALL FOR FEATURE CORRELATION PHASE
def drall_test(win, category, imgs, instructions, boxes, cursor):

    pressed = False
    event.clearEvents()
    cursor.clickReset()
    
    instructions.setPos([0, 275])
    instructions.setText('Which of the following aliens is a better example of a {}?'.format(category))
    instructions.draw()
    
    xcord = [-250, 250]
    rnd.shuffle(xcord)

    for i in range(len(boxes)):
        boxes[i].setPos([xcord[i], 0])
        boxes[i].draw()
        imgs[i].setPos([xcord[i], 0])
        imgs[i].draw()

    win.flip()

    while pressed == False:
        
        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
            
        elif cursor.isPressedIn(boxes[0], buttons=[0,1,2]):
            
            result = 1
            core.wait(1)
            pressed = True
        
        elif cursor.isPressedIn(boxes[1], buttons=[0,1,2]):
            
            result = 0
            core.wait(1)
            pressed = True

    return result

    
## TEST KITCHEN
