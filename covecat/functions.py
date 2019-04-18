# IMPORT DEPENDENCIES
from psychopy import core, event, gui
import os
import pandas as pd
import random as rnd
from time import strftime

# COLLECT USER/EXPERIMENT METADATA

def prompt():

    myDlg = gui.Dlg(title = 'Cove Cat')
    myDlg.addText('Subject Info')
    myDlg.addField('ID:')
    myDlg.addField('Condition:', choices=[0,1])
    myDlg.show()
    
    # quit if participant does not click 'ok' or pnum blank
    if not myDlg.OK or str(myDlg.data[0]) == '':
        core.quit()
    else:
        pnum = str(myDlg.data[0])
        cnd = myDlg.data[1]

        data = pd.DataFrame(columns=['pnum','condition','phase','block','trial','category','item','result']) 

    return [data, pnum, cnd]

# SAVE DATA TO CSV

def save_data(data, subject_dir, pnum, cnd):

    time_stamp = strftime('%Y-%m-%d')
    filename = os.path.join(subject_dir,'covecat_{}_{}_{}.csv'.format(str(cnd), pnum, time_stamp))

    while os.path.exists(filename) == True:
        filename[:-4] += '_dupe.csv'

    data.to_csv(filename,index=False)
    
# SPLASH SCREEN WITH TEXT, WAIT FOR BUTTON PRESS TO ADVANCE

def transition(win, instructions, data):

    phase1 = 'Thank you for participating in the following experiment...\n\nWhen you are ready to get started, please press the SPACEBAR.'

    phase2 = '...'

    test = 'For this next task...'
    
    goodbye = 'You\'ve reached the end of this experiment.\n\nWhen you are ready, please press the SPACEBAR to close this program. Be sure to notify the experimenter that you have concluded this study.'

    instructions.setPos([0, 100])

    if len(data)==0:
        instructions.setText(phase1)
    elif len(data)<25:
        instructions.setText(phase2)
    elif len(data)<65:
        instructions.setText(test)
    else:
        instructions.setText(goodbye)

    instructions.draw()
    win.flip()

    resume=event.waitKeys(keyList=['space', 'escape'])
    if resume[0][0]=='escape':
        win.close()
        core.quit()


def draw_all(win, stim, text, resp_labels, boxes, cursor):

    pressed=False
    
    text.setPos([0, 275])
    text.setText('Is the following ... a ... or ...?')
    text.draw()

    xcord=[-250, 250]
    rnd.shuffle(xcord)

    for options in range(len(resp_labels)):
        boxes[options].setPos([xcord[options], -300])
        boxes[options].draw()
        text.setText(resp_labels[options])
        text.setPos([xcord[options], -300])
        text.draw()

    stim.setPos([0, 0])
    stim.draw()
   
    win.flip()

    while pressed==False:

        text.setPos([0, 275])
        
        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
            
        elif cursor.isPressedIn(boxes[0], buttons=[0,1]):
            
            result=1

            text.setText('Correct! This ... is a(n) {}.'.format(resp_labels[0]))
            text.draw()
            stim.draw()
            win.flip()
            core.wait(3)

            pressed=True
        
        elif cursor.isPressedIn(boxes[1], buttons=[0,1]):
            
            result=0

            text.setText('Inorrect! This ... is a(n) {}.'.format(resp_labels[0]))
            text.draw()
            stim.draw()
            win.flip()
            core.wait(3)

            pressed=True

    return result


def draw_all_test(win, stim, text, resp_labels, boxes, cursor):

    pressed=False
    
    text.setPos([0, 275])
    text.setText('Is the following ... a ..., ..., or ...?')
    text.draw()

    xcord=[-320, 0, 300]
    rnd.shuffle(xcord)

    for options in range(len(resp_labels)):
        boxes[options].setPos([xcord[options], -300])
        boxes[options].draw()
        text.setText(resp_labels[options])
        text.setPos([xcord[options], -300])
        text.draw()

    stim.setPos([0, 0])
    stim.draw()
   
    win.flip()

    while pressed==False:

        text.setPos([0, 275])
        
        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
            
        elif cursor.isPressedIn(boxes[0], buttons=[0,1]):
            
            result=1
            pressed=True
        
        elif cursor.isPressedIn(boxes[1], buttons=[0,1]):
            
            result=0
            pressed=True

    return result
