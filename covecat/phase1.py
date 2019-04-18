# IMPORT MODULES/PACKAGES
import pandas as pd

# DISPLAY WELCOME AND GENERAL INSTRUCTION SCREEN
fx.transition(win, text, data)

# SET PHASE VARIABLE
phase = 'classification_1'
n_blocks = range(1,3)

# DEFINE CATEGORIES, STIM

## create list with all possible stim categories
class_list = sorted(['A','B']*6)

## create dictionary with corresponding stimulus values
stim_dict = {'correct_category': class_list,
             'incorrect_category': class_list[::-1],
             'dimensions': [40, 50, 60, 80, 100, 110, 120, 140, 160, 180, 190, 200],
             'rgb': [-0.8, -0.7, -0.6, -0.4, -0.2, -0.1, 0, 0.1, 0.2, 0.4, 0.6, 0.8]}

## dictionary to dataframe
stim_frame = pd.DataFrame(stim_dict)

# ITERATE THROUGH BLOCKS
for block in n_blocks:
        
	## shuffle rows in dataframe
	stim_frame = stim_frame.sample(frac=1).reset_index(drop=True)

        for n_trials in range(stim_frame.shape[0]):

                ## assign item values
                shape = stim_frame.loc[n_trials, 'dimensions']
                shading = stim_frame.loc[n_trials, 'rgb']

                ## create stim
                stim = visual.Rect(win, units='pix', width=shape, height=shape, fillColorSpace='rgb', lineColorSpace='rgb', fillColor=shading, lineColor=shading)

                ## assign labels
                correct = stim_frame.loc[n_trials, 'correct_category']
                incorrect = stim_frame.loc[n_trials, 'incorrect_category']
                resp_labels = [correct, incorrect]

                # draw window, query response
                result = fx.draw_all(win, stim, text, resp_labels, boxes, cursor)
        
                # update datafile w/trial response
                data.loc[data.shape[0]] = [pnum, cnd, phase, block, n_trials+1, correct, str(shape) + str(shading), result]
