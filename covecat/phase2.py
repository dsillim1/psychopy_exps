# DISPLAY INSTRUCTION SCREEN
fx.transition(win, text, data)

# SET PHASE VARIABLE
phase = 'classification_2'
trial_n = 0

# DEFINE INCORRECT RESPONSE, LOAD STIM
correct_resp = {'A':'ALPHA', 'C':'OMEGA'}
incorrect_resp = {'A':'OMEGA', 'C':'ALPHA'}

class_labels = incorrect_resp.values()

if cnd==0: #control
	cnd_dir = 'train2_c0'
else:
	cnd_dir = 'train2_c1'

train2_dir = os.path.join(stimuli_dir, cnd_dir)
train2_stim = [img for img in os.listdir(train2_dir) if img.endswith('.png')]

# ITERATE THROUGH BLOCKS
for block in n_blocks:
		
	## shuffle stim
	random.shuffle(train2_stim)

	for trial in train2_stim:

		trial_n += 1

		random.shuffle(class_labels)

		## assign stim
		image.setImage(os.path.join(train2_dir, trial))

		## assign labels
		file_name = trial.split('_')

		correct = correct_resp[file_name[0]]
		incorrect = incorrect_resp[file_name[0]]
		resp_labels = [correct, incorrect]

		## draw window, query response
		result = fx.draw_all(win, image, text, resp_labels, class_labels, boxes, cursor)

		## update datafile w/trial response
		data.loc[data.shape[0]] = [pnum, cnd, phase, block, trial_n, file_name[0], file_name[1], result]