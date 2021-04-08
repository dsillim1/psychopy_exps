# DEPENDENCIES
import fx # hand-coded functions
import itertools
import os
from psychopy import event, visual
import random

# SPECIFY DIRECTORIES
## path to store data
analyses_dir = os.path.join(os.getcwd(), 'analyses')
subject_dir = os.path.join(analyses_dir, 'data')

## paths to stimuli
stimuli_dir = os.path.join(os.getcwd(), 'stimuli')
a_dir = os.path.join(stimuli_dir, 'A')
b_dir = os.path.join(stimuli_dir, 'B')

# CREATE DATAFRAME, FETCH PARTICIPANT INFO
[data, pnum, cnd] = fx.prompt() # cnd 0 = learn w/no exceptions, 1 = learn w/task relevant exception

# MISCELLANEOUS VARIABLES
rating_number = range(1,3)
class_map = {'A':'ALPHA','B':'BETA'} # useful for switching presented names on the fly

# DEFINE PSYCHOPY ENVIRONMENT VARIABLES
## fundamentals
win = visual.Window(fullscr=True, units='pix', color='#FFFFFF')
img = visual.ImageStim(win, size=(650, 650))
text = visual.TextStim(win, text='', font='High Tower Text', height=30, wrapWidth=1000, color='#000000')
cursor = event.Mouse(win)

## response boxes
rBox1 = visual.Rect(win, width=300, height=150)
rBox2 = visual.Rect(win, width=300, height=150)
button_boxes = [rBox1, rBox2]

## rating scales
scale_rating = visual.RatingScale(win, pos=(0, -350), labels=['Highly dissimilar','Highly similar'], scale=None, low=-50, high=50, markerStart=0, showAccept=False, tickHeight=0, lineColor='#000000', textColor='#000000', stretch=2, singleClick=True)

scale_conf = visual.RatingScale(win, pos=(0, -350), labels=['High confidence, {}'.format(class_map['A']),'High confidence, {}'.format(class_map['B'])], scale=None, low=-50, high=50, markerStart=0, showAccept=False, tickHeight=0, lineColor='#000000', textColor='#000000', stretch=2, singleClick=True)

# CREATE LIST OF STIM FILE NAMES IN ACCORD W/DIRECTORY
As_all = [A for A in os.listdir(a_dir) if A.endswith('.png')] # includes both exceptions

## adjust As by condition
drop = {0:['7-3.png','9-8.png'], 1:'9-8.png', 2:'7-3.png'} 
As = [os.path.join(a_dir, A) for A in As_all if A not in drop[cnd]]

## Bs, totals, and pairs
Bs = [os.path.join(b_dir, B) for B in os.listdir(b_dir) if B.endswith('.png')]
total_set = As + Bs
pairwise = [pair for pair in itertools.combinations(total_set, 2)]


# TRUNCATE SETS WHEN TESTING
if pnum == 'demo':
    random.shuffle(total_set)
    total_set = total_set[0:3]
    random.shuffle(pairwise)
    pairwise = pairwise[0:3]

# EXEC PHASE SCRIPTS 
for phase in ['sim_rate.py','classification.py','sim_rate.py','conf_rate.py']:
    execfile(phase)
    
fx.transition(win, text, 'end', class_map)
fx.save_data(data, subject_dir, pnum, cnd)

