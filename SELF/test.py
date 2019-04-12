## IMPORT MODULES/PACKAGES
import pandas as pd

# RELAY INSTRUCTIONS
ut.transition(win, instructions, data)

# SET PHASE VARIABLE
phase = 'feature_correlation'

# FETCH ITEMS FROM DIRECTORIES
path_correct = os.path.join(stim_path, 'test_correct')
correct_list = [img for img in os.listdir(path_correct) if img.endswith('.png')]
correct_list.sort()

path_incorrect = os.path.join(stim_path, 'test_incorrect')
incorrect_list = [img for img in os.listdir(path_incorrect) if img.endswith('.png')]
incorrect_list.sort()

# CREATE DICTINARY FROM LISTS
DataDict = {'CORRECT':correct_list,
            'INCORRECT':incorrect_list}

# CREATE DATAFRAME FROM DICTIONARY
df = pd.DataFrame.from_dict(DataDict)
df = df[['CORRECT','INCORRECT']] # re-order, dictionaries have no implicit order

# SHUFFLE DATAFRAME
rnd_df = df.sample(frac=1).reset_index(drop=True)

# ITERATE THROUGH BLOCKS /TRIALS
for i in range(len(rnd_df)):

    block = 1 # only 1 block
    trial = i+1

    # set images from dataframe
    target_stim = rnd_df.loc[i][0]
    alt_stim = rnd_df.loc[i][1]
    
    image.setImage(os.path.join(path_correct, target_stim))
    alt_img.setImage(os.path.join(path_incorrect, alt_stim))

    # collect trial metadata
    trial_info = target_stim.split('_')
    category = label_dict[trial_info[1]]
    item = trial_info[2]

    result = ut.drall_test(win, category, imgs, instructions, boxes, cursor)

    # update datafile w/trial response
    data.loc[data.shape[0]] = [pnum,cnd,phase,block,trial,category,item,result] 


# save datafile to workstation
ut.save_data(data, subject_dir, pnum, cnd)
