# SET IDIOSYNCRACTIC PHASE VARIABLES
phase = 'sim_rate_{}'.format(rating_number.pop(0))
block = 1 
trial_n = 0

# DISPLAY INSTRUCTION SCREEN
fx.transition(win, text, phase, class_map)

random.shuffle(pairwise)

# ITERATE THROUGH PAIRS
for left, right in pairwise:

    trial_n += 1

    ## identify trial items and categories
    categories = []
    items = []

    for stim in [left, right]:
        path = stim.replace('\\','/')
        name_aslist = path.split('/')
        categories.append(name_aslist[-2])
        items.append(name_aslist[-1][:-4])

    ## draw trial, store response
    response = fx.rating_similarity(win, left, right, img, text, scale_rating, cursor)

    ## update dataframe
    data.loc[data.shape[0]] = [pnum, cnd, phase, block, trial_n, categories[0], categories[1], items[0], items[1], response[0], response[1]]
