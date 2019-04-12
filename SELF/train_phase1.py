## IMPORT MODULES/PACKAGES
import random as rnd

# SET PHASE VARIABLE
phase = 'classification_1'

# FETCH ITEMS FROM DIR
phase_path = os.path.join(stim_path, 'train_all')
train_all = [img for img in os.listdir(phase_path) if img.endswith('.png')]

# SET UP DICTIONARY FOR QUICK LABEL SWITCHING 
label_dict = {'A':'MAKMAK','B':'SWIB'}

# ITERATE THROUGH BLOCKS /TRIALS
for i in range(2):

    block = i+1

    # randomize stim order
    rnd.shuffle(train_all)

    for j in range(len(train_all)):
        
        trial = j+1

        # set image
        trial_stim = train_all[j]
        image.setImage(os.path.join(phase_path, trial_stim))

        #collect trial metadata
        trial_info = trial_stim.split('_')
        category = label_dict[trial_info[0]]
        item = trial_info[1]

        # set labels
        correct.setText(category)

        if category == label_dict['A']:
            compliment = label_dict['B']
        else:
            compliment = label_dict['A']
        
        incorrect.setText(compliment)

        # draw window, query response
        result = ut.draw_all(win, category, image, instructions, boxes, labels, cursor)
        
        # update datafile w/trial response
        data.loc[data.shape[0]] = [pnum,cnd,phase,block,trial,category,item,result] 
