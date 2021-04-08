# INTERNAL DEPENDENCIES
import os

# EXTERNAL ...
import fx # local
from psychopy import event, visual

# SET UP RELEVANT PATHS, SEED DATA MATRIX
analyses_dir = os.path.join(os.getcwd(), 'analyses')
subject_dir = os.path.join(analyses_dir, 'data')

## stim paths
stimuli_dir = os.path.join(os.getcwd(), 'stimuli')
standard_dir = os.path.join(stimuli_dir, 'standard')
rel_dir = os.path.join(stimuli_dir, 'rel_match')
sup_dir = os.path.join(stimuli_dir, 'sup_match')

## fetch participant info
[data, pnum, cnd] = fx.prompt()

# DEFINE PSYCHOPY ENVIRONMENT VARIABLES
win = visual.Window(fullscr=True, units='pix', color='#afabab')

img_stn = visual.ImageStim(win, size=(250, 250))
img_stn.setPos([0, -250])
img_sup = visual.ImageStim(win, size=(250, 250))
img_rel = visual.ImageStim(win, size=(250, 250))
comparison_list = [img_sup, img_rel]

xcord = [-250, 250]
text = visual.TextStim(win, text='', font='High Tower Text', height=30, wrapWidth=800, color='#000000')
cursor = event.Mouse(visible=True, newPos=None, win=win)

## response boxes
rBox1 = visual.Rect(win, width=300, height=300, lineColor='#afabab')
rBox2 = visual.Rect(win, width=300, height=300, lineColor='#afabab')
boxes = [rBox1, rBox2]

## create list of stim file names per directory
standards = [img for img in os.listdir(standard_dir) if img.endswith('.png')]
rMatch = [img for img in os.listdir(rel_dir) if img.endswith('.png')]
sMatch = [img for img in os.listdir(sup_dir) if img.endswith('.png')]

# SET DICTIONARY OF TRIAL FUNCTIONS PAIRED WITH CONDITIONS
trial_type = {1:fx.sim_trial,
              2:fx.seq1_trial,
              3:fx.seq2_trial}

# EXEC PHASE SCRIPTS 
for phase in ['train.py']:
    execfile(phase)

fx.save_data(data, subject_dir, pnum, cnd)
