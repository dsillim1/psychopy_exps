# INTERNAL DEPENDENCIES
import os

# EXTERNAL ...
import functions as fx # local
import psychopy as psy

# SEED DATAFILE, QUERY CONDITION
subject_dir = os.path.join(os.getcwd(), 'data')
[data, pnum, cnd] = fx.prompt()

# DEFINE PSYCHOPY ENVIRONMENT VARIABLES

win = psy.visual.Window(fullscr=True, units='pix', color=(1, 1, 1))
stim = psy.visual.Rect(win, width=0, height=0) # fill
text = psy.visual.TextStim(win, text='', font='High Tower Text', height=30, wrapWidth=800, color=(0, 0, 0))
cursor = psy.event.Mouse(visible=True, newPos=None, win=win)

# RESPONSE BOXES
rBox1 = psy.visual.Rect(win, width=300, height=300)
rBox2 = psy.visual.Rect(win, width=300, height=300)
boxes = [rBox1, rBox2]

# EXEC PHASE SCRIPTS
for i in ['phase1.py','phase2.py','test.py']:
    execfile(i)