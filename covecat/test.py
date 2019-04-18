# DISPLAY WELCOME AND GENERAL INSTRUCTION SCREEN
fx.transition(win, text, data)

# SET PHASE VARIABLE
phase = 'generalization'



# DEFINE CATEGORIES, STIM

## create list with all possible stim categories
item_type = sorted(['critical']*6 + ['non-critical']*9) ## UPDATE HERE

## create dictionary with corresponding stimulus values
stim_dict = {'item_type': item_type,
             'dimensions': [45.5, 66, 86.5, 189, 209.5, 230, 66, 66, 66, 209.5, 209.5, 209.5, 66, 66, 66],
             'rgb': [5.26, 5.26, 5.26, 5.26, 5.26, 5.26, 2.96, 3.42, 3.88, 2.96, 3.42, 3.88, 6.18, 6.64, 7.1]}

# ADD RESPONSE BOX
rBox3 = visual.Rect(win, width=300, height=300)
boxes.append(rBox3)

## dictionary to dataframe
stim_frame = pd.DataFrame(stim_dict)

## shuffle rows in dataframe
stim_frame = stim_frame.sample(frac=1).reset_index(drop=True)

for n_trials in range(stim_frame.shape[0]):

        ## assign item values
        shape = stim_frame.loc[n_trials, 'dimensions']
        shading = stim_frame.loc[n_trials, 'rgb']

        ## create stim
        stim = visual.Rect(win, units='cm', width=shape, height=shape, fillColorSpace='rgb', lineColorSpace='rgb', fillColor=shading, lineColor=shading)

        ## assign labels
        resp_labels = ['A', 'B', 'C']

        # draw window, query response
        result = fx.draw_all(win, stim, text, resp_labels, boxes, cursor)

        # update datafile w/trial response
        data.loc[data.shape[0]] = [pnum, cnd, phase, 1, n_trials+1, stim_frame.loc[n_trials, 'item_type'], str(shape) + str(shading), result] 
        
