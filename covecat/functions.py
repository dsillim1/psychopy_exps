# IMPORT DEPENDENCIES
from psychopy import core, event, gui
import os
import pandas as pd
import random
from time import strftime

# COLLECT USER/EXPERIMENT METADATA

def prompt():

    myDlg = gui.Dlg(title = 'Cove Cat')
    myDlg.addText('Subject Info')
    myDlg.addField('ID:')
    myDlg.addField('Condition:', choices=range(2))
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
        filename = filename[-4]
        filename += '_dupe.csv'

    data.to_csv(filename,index=False)
    
# SPLASH SCREEN WITH TEXT, WAIT FOR BUTTON PRESS TO ADVANCE

def transition(win, instructions, data):

    classes = {'A':'ALPHA', 'B':'BETA', 'C':'OMEGA'} # useful for quickly swapping names in event of lab conflict

    phase1 = 'Thank you for participating in the following experiment.\n\nIn your first task, you will be shown examples of various squares. The examples belong to two different kinds, and your job is to learn to tell which ones are from which category: {}s and {}s.\n\nAs you are shown each example, you will be asked to decide its category. You will receive feedback on each trial to help you learn. At first you will just have to guess, but you will gain experience as you go. It may not be easy, but before long, you should develop a good sense of the two categories.\n\nWhen you are ready to get started, please press the SPACEBAR.'.format(classes['A'], classes['B'])

    phase2 = 'For this next task, your goal is to learn how to tell {}s from a new category of squares: {}s. The former category of {}s will no longer appear for now, though they will show up on the subsequent task. Some of the {}s will be the same from the prior task, and some will be different. Other than the new examples, your task is the same.\n\nWhen you are ready to get started, please press the SPACEBAR.'.format(classes['A'], classes['C'], classes['B'], classes['A'])

    test = 'For this last task, you will be seeing new examples which belong to either of the formerly learned categories: {}s, {}s, and {}s. You now have three response options and will receive no feedback after making a choice. Aside from these changes, the task is the same as before.\n\nWhen you are ready to get started, please press the SPACEBAR.'.format(classes['A'], classes['B'], classes['C'])
    
    goodbye = 'You\'ve reached the end of this experiment. Thank you for your participation.\n\nWhen you are ready, please press the SPACEBAR to close this program. Be sure to notify the experimenter that you have concluded this study.'

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


def draw_all(win, stim, text, resp_labels, class_labels, boxes, cursor):

    pressed=False
    
    stim.setPos([0, 0])
    stim.draw()

    text.setPos([0, 375])
    text.setText('Is the following square a(n) {} or {}?'.format(*class_labels))
    text.draw()

    xcord=[-250, 250]
    random.shuffle(xcord)

    for options in range(len(resp_labels)):
        boxes[options].setPos([xcord[options], -350])
        boxes[options].draw()
        text.setText(resp_labels[options])
        text.setPos([xcord[options], -350])
        text.draw()
   
    win.flip()

    while pressed==False:

        text.setPos([0, 375])
        
        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
            
        elif cursor.isPressedIn(boxes[0], buttons=[0,1]):
            
            result=1

            text.setText('Correct! This square is a(n) {}.'.format(resp_labels[0]))
            text.draw()
            stim.draw()
            win.flip()
            core.wait(3)

            pressed=True
        
        elif cursor.isPressedIn(boxes[1], buttons=[0,1]):
            
            result=0

            text.setText('Incorrect! This square is a(n) {}.'.format(resp_labels[0]))
            text.draw()
            stim.draw()
            win.flip()
            core.wait(3)

            pressed=True

    return result


def draw_all_test(win, stim, text, resp_labels, class_labels, boxes, cursor):

    pressed=False

    stim.setPos([0, 0])
    stim.draw()

    text.setPos([0, 375])
    text.setText('Is the following square a {}, {}, or {}?'.format(*class_labels))
    text.draw()

    xcord=[-420, 0, 420]
    random.shuffle(xcord)

    for options in range(len(resp_labels)):
        boxes[options].setPos([xcord[options], -350])
        boxes[options].draw()
        text.setText(resp_labels[options])
        text.setPos([xcord[options], -350])
        text.draw()
   
    win.flip()

    while pressed==False:

        text.setPos([0, 375])
        
        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
            
        elif cursor.isPressedIn(boxes[0], buttons=[0,1]):
            
            result='A'
            core.wait(1)
            pressed=True
        
        elif cursor.isPressedIn(boxes[1], buttons=[0,1]):
            
            result='B'
            core.wait(1)
            pressed=True

        elif cursor.isPressedIn(boxes[2], buttons=[0,1]):
            
            result='C'
            core.wait(1)
            pressed=True
            
    return result
