# IMPORT DEPENDENCIES
from psychopy import gui, core, visual, event
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

    hello = 'Thank you for participating in the following experiment...\n\nWhen you are ready to get started, please press the SPACEBAR.'

    test = 'For this next task...'
    
    goodbye = 'You\'ve reached the end of this experiment.\n\nWhen you are ready, please press the SPACEBAR to close this program. Be sure to notify the experimenter that you have concluded this study.'

    instructions.setPos([0, 100])

    if len(data) == 0:
        instructions.setText(hello)
    elif len(data) < 45:
        instructions.setText(test)
    else:
        instructions.setText(goodbye)

    instructions.draw()
    win.flip()

    resume = event.waitKeys(keyList=['space', 'escape'])
    if resume[0][0] == 'escape':
        win.close()
        core.quit()
