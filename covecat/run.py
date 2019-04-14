# INTERNAL DEPENDENCIES
import os

# EXTERNAL ...
import functions as fx # local
from psychopy import event, visual

# SEED DATAFILE, QUERY CONDITION
subject_dir = os.path.join(os.getcwd(), 'data')
[data, pnum, cnd] = fx.prompt()

# DEFINE PSYCHOPY ENVIRONMENT VARIABLES

win = visual.Window(fullscr=True, units='pix', color=(1, 1, 1))
stim = visual.Rect(win, width=0, height=0) # fill
text = visual.TextStim(win, text='', font='High Tower Text', height=30, wrapWidth=800, color=(0, 0, 0))
cursor = event.Mouse(visible=True, newPos=None, win=win)

# RESPONSE BOXES
rBox1 = visual.Rect(win, width=300, height=300)
rBox2 = visual.Rect(win, width=300, height=300)
boxes = [rBox1, rBox2]

# EXEC PHASE SCRIPTS
for i in ['phase1.py','phase2.py','test.py']:
    execfile(i)