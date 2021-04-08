# IMPORT DEPENDENCIES
from psychopy import core, event, visual
import os
import fx
from materials import *
import random

# SPECIFY DIRECTORIES
## path to store data
analyses_dir = os.path.join(os.getcwd(), 'analyses')
subject_dir = os.path.join(analyses_dir, 'data')

# CREATE DATAFRAME, FETCH PARTICIPANT INFO
[data, pnum] = fx.prompt() 

# DEFINE PSYCHOPY ENVIRONMENT VARIABLES
## fundamentals
win = visual.Window(fullscr=True, units='pix', color='#FFFFFF')
box = visual.Rect(win, width=500, height=200, lineColor='black')
text = visual.TextStim(win, text='', font='High Tower Text', height=30, wrapWidth=475, color='#000000')
box_two = visual.Rect(win, width=500, height=200, lineColor='black')
text_two = visual.TextStim(win, text='', font='High Tower Text', height=30, wrapWidth=475, color='#000000')
text_three = visual.TextStim(win, text='', font='High Tower Text', height=30, wrapWidth=1200, pos=(0,0), color='#000000')
cursor = event.Mouse(win)
timer = core.Clock()

## rating scale
scale_rating = visual.RatingScale(win, pos=(0, -350), labels=['Not at all similar','Highly similar'], scale=None, low=-50, high=50, markerStart=0, showAccept=False, acceptText='continue', tickHeight=0, lineColor='#000000', textColor='#000000', stretch=2, singleClick=True)

## create pairings for similarity ratings
pairs = fx.gen_order(pairwise)

## miscallaneous variables
preMZero = ''
preMTwo = ''

# TRUNCATE SETS WHEN TESTING
if pnum == 'demo':

    random.shuffle(pairs)

    preMZero = [target for target in pairs if target[1][2] == 'M0']
    preMZero = random.choice(preMZero)
    preMZero[1][4] = 1

    preMTwo = [target for target in pairs if target[1][2] == 'M2']
    preMTwo = random.choice(preMTwo)
    preMTwo[1][4] = 1

    pairs = pairs[0:3]

# PRE-EXPOSURE PHASE
inst_token = 0
inst_token = fx.transition(win, text_three, inst_token)

if preMZero == '':
    preMZero = [target for target in pairs if target[1][2] == 'M0']
    preMZero = random.choice(preMZero)
    pairs.remove(preMZero)
    preMZero[1][4] = 1

    preMTwo = [target for target in pairs if target[1][2] == 'M2']
    preMTwo = random.choice(preMTwo)
    pairs.remove(preMTwo)
    preMTwo[1][4] = 1

pre_pairs = [preMZero, preMTwo]
random.shuffle(pre_pairs)

for pair in pre_pairs:
    
	## get trial data
	ratings = fx.compare(win, pair, text, text_two, text_three, box, box_two, timer, scale_rating)

	## update dataframe
	data.loc[data.shape[0]] = [pnum, 0, pair[1][1], pair[1][2], pair[1][3], pair[1][4], ratings[0], ratings[1], ratings[2]]

# COMPARISON PHASE
inst_token = fx.transition(win, text_three, inst_token)

for pair in pairs:

	tnum = pairs.index(pair) + 1

	## get trial data
	ratings = fx.compare(win, pair, text, text_two, text_three, box, box_two, timer, scale_rating)

	## update dataframe
	data.loc[data.shape[0]] = [pnum, tnum, pair[1][1], pair[1][2], pair[1][3], pair[1][4], ratings[0], ratings[1], ratings[2]]

    
inst_token = fx.transition(win, text_three, inst_token)
fx.save_data(data, subject_dir, pnum)

