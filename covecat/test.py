# DISPLAY INSTRUCTION SCREEN
fx.transition(win, text, data)

# SET PHASE VARIABLE
phase = 'generalization'

# DICTIONARY FOR ITEM TYPE
item_type = {'C':'OMEGA', 'B':'BETA' 'N':'Non-critical'}

class_labels = ['ALPHA', 'BETA', 'OMEGA']

test_dir = os.path.join(stimuli_dir, 'test')
test_stim = [img for img in os.listdir(test_dir) if img.endswith('.png')]

# ADD RESPONSE BOX
rBox3 = visual.Rect(win, width=300, height=300)
boxes.append(rBox3)

## shuffle rows in dataframe
random.shuffle(test_stim)

for trial in test_stim:

	random.shuffle(class_labels)

	## assign stim
	image.setImage(os.path.join(test_dir, trial))

	## grab file name for item data
	file_name = trial.split('_')

	# draw window, query response
	result = fx.draw_all_test(win, image, text, class_labels, class_labels, boxes, cursor)

	# update datafile w/trial response
	data.loc[data.shape[0]] = [pnum, cnd, phase, 1, test_stim.index(trial), item_type[file_name[0]], file_name[1], result] 
		
# DISPLAY FAREWELL SCREEN
fx.transition(win, text, data)