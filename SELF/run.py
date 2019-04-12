## IMPORT MODULES/PACKAGES
from psychopy import event, visual
import os
import utils as ut

## SEED DATAFILES, QUERY CONDITION:
subject_dir = os.path.join(os.getcwd(), 'data')
[data, pnum, cnd] = ut.prompt()

## DEFINE PSYCHOPY ENVIRONMENT VARIABLES
win = visual.Window(fullscr=True, units='pix', color=(1, 1, 1))

# IMAGES
image = visual.ImageStim(win, size=(450,450))
alt_img = visual.ImageStim(win, size=(450,450))
imgs = [image, alt_img]

# TEXT
instructions = visual.TextStim(win, text='', font='High Tower Text', height=30, wrapWidth=800, color=(0, 0, 0))
correct = visual.TextStim(win, text='', font='High Tower Text', height=30, wrapWidth=800, color=(0, 0, 0))
incorrect = visual.TextStim(win, text='', font='High Tower Text', height=30, wrapWidth=800, color=(0, 0, 0))
labels = [correct, incorrect]

# MOUSE 
cursor = event.Mouse(visible=True, newPos=None, win=win)

# RESPONSE BOXES
rBox1 = visual.Rect(win, width=300, height=300)
rBox2 = visual.Rect(win, width=300, height=300)
boxes = [rBox1, rBox2]

## DEFINE STIMULI PATH
stim_path = os.path.join(os.getcwd(), 'stim')

## DISPLAY WELCOME AND GENERAL INSTRUCTION SCREEN
ut.transition(win, instructions, data)

## EXEC PHASE SCRIPTS
for i in ['train_phase1.py','train_phase2.py','test.py']:
    execfile(i)

## DISPLAY THANK YOU AND ADVANCEMENT SCREEN
ut.transition(win, instructions, data)
