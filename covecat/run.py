# INTERNAL DEPENDENCIES
import os

# EXTERNAL ...
import functions as fx # local
from psychopy import event, visual

# SET UP RELEVANT PATHS, SEED DATAFILE
analysis_dir = os.path.join(os.getcwd(), 'analyses')
subject_dir = os.path.join(analysis_dir, 'data')
stimuli_dir = os.path.join(os.getcwd(), 'stimuli')
[data, pnum, cnd] = fx.prompt()

# DEFINE PSYCHOPY ENVIRONMENT VARIABLES

win = visual.Window(fullscr=True, units='pix', color=(1, 1, 1))
image = visual.ImageStim(win, size=(650, 650))
text = visual.TextStim(win, text='', font='High Tower Text', height=30, wrapWidth=800, color=(0, 0, 0))
cursor = event.Mouse(visible=True, newPos=None, win=win)

# RESPONSE BOXES
rBox1 = visual.Rect(win, width=300, height=300)
rBox2 = visual.Rect(win, width=300, height=300)
boxes = [rBox1, rBox2]

# EXEC PHASE SCRIPTS ,'phase2.py','test.py'
for phase in ['phase1.py', 'phase2.py','test.py']:
    execfile(phase)

fx.save_data(data, subject_dir, pnum, cnd)