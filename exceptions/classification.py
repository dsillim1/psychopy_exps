# SET IDIOSYNCRACTIC PHASE VARIABLES
phase = 'classification'
n_blocks = range(1,4) # set to 3 right now, adjust as needed
trial_n = 0

# DISPLAY INSTRUCTION SCREEN
fx.transition(win, text, phase, class_map)

# ITERATE THROUGH TACL
for block in n_blocks:

    random.shuffle(total_set)

    for trial in total_set:

        trial_n += 1

        ## assign stimulus
        img.setImage(trial)

        ## identify trial item and category
        path = trial.replace('\\','/')
        name_aslist = path.split('/')
        category = name_aslist[-2]
        item = name_aslist[-1][:-4]

        ## assign labels to buttons
        all_classes = class_map.values()
        
        correct = class_map[category]
        
        all_classes.remove(correct)
        incorrect = all_classes[0]

        button_labels = [correct, incorrect]

        ## draw trial, store response
        response = fx.classify(win, img, text, button_boxes, button_labels, class_map, cursor)

        ## update dataframe
        data.loc[data.shape[0]] = [pnum, cnd, phase, block, trial_n, category, 'N/A', item, 'N/A', response[0], response[1]]

        
