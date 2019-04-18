# DISPLAY WELCOME AND GENERAL INSTRUCTION SCREEN
fx.transition(win, text, data)

# SET PHASE VARIABLE
phase = 'generalization'

# DEFINE CATEGORIES, STIM

## create list with all possible stim categories
item_type = sorted(['critical','non-critical']*'SOME NUMBER') ## UPDATE HERE

## create dictionary with corresponding stimulus values
stim_dict = {'item_type': item_type,
             'dimensions': [],
             'rgb': []}

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
                resp_labels = ['A', 'B', 'C']

                # draw window, query response
                result = fx.draw_all(win, stim, text, resp_labels, boxes, cursor)
        
                # update datafile w/trial response
                data.loc[data.shape[0]] = [pnum, cnd, phase, block, n_trials+1, stim_frame.loc[n_trials, 'item_type'], str(shape) + str(shading), result] 
        