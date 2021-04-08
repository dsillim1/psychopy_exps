# IMPORT MODULES/PACKAGES
import random

# DISPLAY WELCOME AND GENERAL INSTRUCTION SCREEN
fx.transition(win, text, data)

# SET PHASE VARIABLES
n_blocks = range(1,2) # set to 1 right now, adjust as needed
trial_n = 0
text.setPos([0, 375])
last_match = 'xx'

# ITERATE THROUGH BLOCKS
for block in n_blocks:

    random.shuffle(standards)
    
    for trial in standards:
        
        trial_n += 1

        ## assign stim to image variables
        img_stn.setImage(os.path.join(standard_dir, trial))

        sup_list = [img for img in sMatch if img.startswith('{}'.format(trial[0]))]
        sup_choice = random.choice(sup_list)
        img_sup.setImage(os.path.join(sup_dir, sup_choice))

        while True:
            rel_choice = random.choice(rMatch)
            if rel_choice not in [trial, last_match]:
                break
        last_match = rel_choice[:] # keeps the same stim from appearing twice in a row    
        img_rel.setImage(os.path.join(rel_dir, rel_choice))

        ## draw window, query response
        output = trial_type[cnd](win, img_stn, comparison_list, boxes, xcord, cursor, text)

        ## update datafile w/trial response
        data.loc[len(data),:] = [pnum, cnd, block, trial_n, trial[:-4], rel_choice[:-4], sup_choice[:-4], output[0], output[1]]

# DISPLAY CLOSE SCREEN
fx.transition(win, text, data)
