# IMPORT DEPENDENCIES
from psychopy import core, event, gui, visual
import os
import pandas as pd
import random
from time import strftime

# COLLECT USER/EXPERIMENT METADATA

def prompt():

    myDlg = gui.Dlg(title = 'RMS')
    myDlg.addText('Subject Info')
    myDlg.addField('ID:',21)
    myDlg.addField('Condition:', choices=range(1,4))
    myDlg.show()
    
    # quit if participant does not click 'ok' or pnum blank
    if not myDlg.OK or str(myDlg.data[0]) == '':
        core.quit()
    else:
        pnum = str(myDlg.data[0])
        cnd = myDlg.data[1]

        data = pd.DataFrame(columns=['pnum','condition','block','trial','standard','relational match','superficial match','choice','supplemental']) 

    return [data, pnum, cnd]

# SAVE DATA TO CSV

def save_data(data, subject_dir, pnum, cnd):

    time_stamp = strftime('%Y-%m-%d')
    filename = os.path.join(subject_dir,'rms_{}_{}_{}.csv'.format(str(cnd), pnum, time_stamp))

    while os.path.exists(filename) == True:
        filename = filename[-4]
        filename += '_dupe.csv'

    data.to_csv(filename,index=False)
    
# SPLASH SCREEN WITH TEXT, WAIT FOR BUTTON PRESS TO ADVANCE

def transition(win, instructions, data):

    welcome = 'Thank you for participating in the following experiment.\n\nIn ...\n\nWhen you are ready to get started, please press the SPACEBAR.'
    
    goodbye = 'You\'ve reached the end of this experiment. Thank you for your participation.\n\nWhen you are ready, please press the SPACEBAR to close this program. Be sure to notify the experimenter that you have concluded this study.'
    instructions.setPos([0, 100])

    if len(data)==0:
        instructions.setText(welcome)
    else:
        instructions.setText(goodbye)

    instructions.draw()
    win.flip()

    resume=event.waitKeys(keyList=['space', 'escape'])
    if resume[0][0]=='escape':
        win.close()
        core.quit()

# RUN TRIAL ACCORDING TO CONDITION

def sim_trial(win, standard, comparisons, boxes, xcord, cursor, text):

    pressed = False
    random.shuffle(xcord)

    for n_boxes in range(len(boxes)):

        boxes[n_boxes].setPos([xcord[n_boxes], 150])
        boxes[n_boxes].draw()
        comparisons[n_boxes].setPos([xcord[n_boxes], 150])
        comparisons[n_boxes].draw()

    standard.draw()
    text.setText('What\'s the best match?')
    text.draw()
    
    win.flip()

    while pressed==False:

        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
            
        elif cursor.isPressedIn(boxes[0], buttons=[0,1]):
            
            result=0
            core.wait(1)
            pressed=True
        
        elif cursor.isPressedIn(boxes[1], buttons=[0,1]):
            
            result=1
            core.wait(1)
            pressed=True

    return [result, 'N/A']


# first one pair, then the other         
def seq1_trial(win, standard, comparisons, boxes, xcord, cursor, text):

    pressed = False

    copy_comparisons = list(comparisons)
    random.shuffle(copy_comparisons)
    random.shuffle(xcord)

    if copy_comparisons[0] == comparisons[0]:
        first='superficial'
    else:
        first='relational'
    
    # draw stim
    for n_matches in range(len(copy_comparisons)):
        copy_comparisons[n_matches].setPos([xcord[n_matches], 150])
        place = comparisons.index(copy_comparisons[n_matches])
        boxes[place].setPos([xcord[n_matches], 150])
        copy_comparisons[n_matches].draw()
        text.setText('What do the following pair have in common?')
        text.draw()
        standard.draw()
        win.flip()
        core.wait(3)

    for n_boxes in range(len(boxes)):

        boxes[n_boxes].draw()
        copy_comparisons[n_boxes].draw()

    standard.draw()
    text.setText('What\'s the best match?')
    text.draw()
    
    win.flip()

    while pressed==False:

        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
            
        elif cursor.isPressedIn(boxes[0], buttons=[0,1]):
            
            result=0
            core.wait(1)
            pressed=True
        
        elif cursor.isPressedIn(boxes[1], buttons=[0,1]):
            
            result=1
            core.wait(1)
            pressed=True

    return [result, first]


# User response fx, courtesy of Matt
def seq2_trial(win, standard, comparisons, boxes, xcord, cursor, text):

    quit_keys=['escape']

    text.setText('Using the keyboard, describe the stimulus on-screen. When you are satisified with your answer, press the HOME key to continue.')
    
    # This variable will act as a container for the user's response; and will be frequently adjusted
    response_text = visual.TextStim(win, text='...', height=22, font='High Tower Text', color='#000000', pos=[0, 0], wrapWidth=1000)

    
    ##__Start Process
    event.clearEvents()
    cursor.clickReset() # probably not necessary 

    ## Put the visual objects on the upcoming window
    standard.draw()
    text.draw()
    response_text.draw()
    win.flip() # show the window

    response = [] # holds all the button press information
    
    while True:
        
        # Check to make sure user hasn't press a quit key
        if event.getKeys(keyList=[quit_keys]):
            core.quit()

        # Again check to make sure user isn't pressing a quit key
        key_press = event.waitKeys()

        if key_press[0] in quit_keys:
            core.quit()

        # end process once once user presses the enter/return key
        if key_press == ['home']:
            description = ''.join(response) # returns a string of all characters in 'response' variable
            break

        else:
            if key_press == ['backspace']: # delete last item if user pressed backspace
                if len(response) == 0: # but don't do anything if they haven't typed anything in yet
                    pass
                else:
                    response = response[:-1]
            else:
                for key in key_press: # add key_press to "response" list (which is a list of letters)
                    if len(key) == 1: # i think this ensures that it only records single characters (otherwise, it'll record 'tab', 'return', etc)
                        response.append(key_press[0])
                    elif key == 'space':
                        response.append(' ')
                    elif key == 'period':
                        response.append('.')
                    elif key == 'slash':
                        response.append('/')
                    elif key == 'semicolon':
                        response.append(';')
                    elif key == 'apostrophe':
                        response.append("'")
                    elif key == 'comma':
                        response.append(',')

        response_string = ''.join(response) # convert list of letters into a single string
        response_text.setText(response_string) # set the recorded response as the text for the response_text variable (container) that will appear on screen

        # draw everything again
        standard.draw()
        response_text.draw() # put the response_text variable on the upcoming window
        text.draw() # redraw the instructions to the upcoming window
        win.flip() # replace the old window with the new window


    core.wait(1)
    
    random.shuffle(xcord)

    for n_boxes in range(len(boxes)):

        boxes[n_boxes].setPos([xcord[n_boxes], 150])
        boxes[n_boxes].draw()
        comparisons[n_boxes].setPos([xcord[n_boxes], 150])
        comparisons[n_boxes].draw()

    standard.draw()
    text.setText('What\'s the best match?')
    text.draw()
    
    win.flip()

    pressed = False

    while pressed==False:

        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
            
        elif cursor.isPressedIn(boxes[0], buttons=[0,1]):
            
            result=0
            core.wait(1)
            pressed=True
        
        elif cursor.isPressedIn(boxes[1], buttons=[0,1]):
            
            result=1
            core.wait(1)
            pressed=True

    return [result, description]

# standard has descriptive text
def seqOLD_trial(win, standard, comparisons, boxes, xcord, cursor, text): # DELETE ME

    pressed = False

    standard.draw()

    # instructions
    text.setText('Using the keyboard, describe the stimulus on-screen. When you are satisified with your answer, press the HOME key to continue.')
    text.draw()
    
    win.flip()
    core.wait(4)

    random.shuffle(xcord)

    for n_boxes in range(len(boxes)):

        boxes[n_boxes].setPos([xcord[n_boxes], 150])
        boxes[n_boxes].draw()
        comparisons[n_boxes].setPos([xcord[n_boxes], 150])
        comparisons[n_boxes].draw()

    standard.draw()
    text.setText('What\'s the best match?')
    text.draw()
    
    win.flip()

    while pressed==False:

        if event.getKeys(keyList='escape'):
            win.close()
            core.quit()
            
        elif cursor.isPressedIn(boxes[0], buttons=[0,1]):
            
            result=0
            core.wait(1)
            pressed=True
        
        elif cursor.isPressedIn(boxes[1], buttons=[0,1]):
            
            result=1
            core.wait(1)
            pressed=True

    return [result, description]
