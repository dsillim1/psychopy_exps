# Import dependencies
from psychopy import event, visual
import os
import pandas as pd
import random as rnd
import functions as fx

## SEED DATAFILES, QUERY CONDITION:
subject_dir = os.path.join(os.getcwd(), 'data')
[data, pnum, cnd] = fx.prompt()








## EXEC PHASE SCRIPTS
for i in ['phase1.py','phase2.py','test.py']:
    execfile(i)

## DISPLAY THANK YOU AND ADVANCEMENT SCREEN
fx.transition(win, instructions, data)

