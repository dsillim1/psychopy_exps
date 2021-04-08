# SET IDIOSYNCRACTIC PHASE VARIABLES
phase = 'conf_rate'
block = 1 
trial_n = 0

# DISPLAY INSTRUCTION SCREEN
fx.transition(win, text, phase, class_map)

random.shuffle(total_set)

# ITERATE THROUGH SET
for trial in total_set:

    trial_n += 1

    ## assign stimulus
    img.setImage(trial)

    ## identify trial item and category
    path = trial.replace('\\','/')
    name_aslist = path.split('/')
    category = name_aslist[-2]
    item = name_aslist[-1][:-4]

    ## draw trial, store response
    response = fx.rating_confidence(win, img, text, scale_conf, cursor)

    ## update dataframe
    data.loc[data.shape[0]] = [pnum, cnd, phase, block, trial_n, category, 'N/A', item, 'N/A', response[0], response[1]]
