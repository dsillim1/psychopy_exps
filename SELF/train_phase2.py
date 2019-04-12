# Set phase variables
phase = 'classification_2'

# fetch items according to condition
if cnd == 1:
    stim = train_all 
else:
    phase_path = os.path.join(stim_path, 'train_exp')
    stim = [img for img in os.listdir(phase_path) if img.endswith('.png')]


for i in range(3, 4):

    block = i+1

    # randomize stim order
    rnd.shuffle(stim)

    for j in range(len(stim)):
        
        trial = j+1

        # set image
        trial_stim = stim[j]
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

