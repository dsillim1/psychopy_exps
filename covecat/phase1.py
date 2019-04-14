# IMPORT MODULES/PACKAGES
import pandas as pd
import random as rnd

# DISPLAY WELCOME AND GENERAL INSTRUCTION SCREEN
fx.transition(win, text, data)

# SET PHASE VARIABLE
phase = 'classification_1'

# DEFINE CATEGORIES, STIM

## create list with all possible stim categories
class_list = sorted(range(1,3)*4)

## create dictionary with corresponding stimulus values
stim_dict = {'correct_category':class_list,
			 'incorrect_category':class_list[::-1],
			 'dimensions':[],
			 'rgb':[]}

## dictionary to dataframe
stim_frame = pd.DataFrame(data = stim_dict)


# ITERATE THROUGH BLOCKS

for n_blocks in range(2):
	
	## shuffle rows in dataframe
	stim_frame = stim_frame.sample(frac=1).reset_index(drop=True)