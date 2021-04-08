# IMPORT DEPENDENCIES
from psychopy import core, event, gui, visual
import os
import pandas as pd
import random
from time import strftime
import copy

# COLLECT USER/EXPERIMENT METADATA

def prompt():

    myDlg = gui.Dlg(title = 'RShep')
    myDlg.addText('Subject Info')
    myDlg.addField('ID:')
    myDlg.show()
    
    # quit if participant does not click 'ok' or pnum blank
    if not myDlg.OK or str(myDlg.data[0]) == '':
        core.quit()
    else:
        pnum = str(myDlg.data[0])
        data = pd.DataFrame(columns=['pnum','trial','set','match','form','training','base position','rating','rt']) 

    return [data, pnum]

# SAVE DATA TO CSV

def save_data(data, subject_dir, pnum):

    time_stamp = strftime('%Y-%m-%d')
    filename = os.path.join(subject_dir,'rms_{}_{}.csv'.format(pnum, time_stamp))

    while os.path.exists(filename) == True:
        filename = filename[-4]
        filename += '_dupe.csv'

    data.to_csv(filename, index=False)
    
# SPLASH SCREEN WITH TEXT, WAIT FOR BUTTON PRESS TO ADVANCE

def transition(win, instructions, token):

    pre_exp = 'Thank you for participating in the following experiment.\n\nOn each trial of this experiment, you will see two sentences presented side-by-side. Read each sentence, then consider how similar the two sentences are. You may indicate your response using a continuous rating scale. There will be no individual numbers associated with the scale, but please don\'t hesitate to use the entire range of the scale. On the next two screens we will provide you with two practice examples so that you may get familiar with the task. \n\nWhen you are ready to get started, please press the SPACEBAR.'
    rating = 'The practice phase has concluded. If you have any questions, please ask the research assistant now. If not, please press the SPACEBAR to continue to the real task.'
    goodbye = 'You\'ve reached the end of this experiment. Thank you for your participation.\n\nWhen you are ready, please press the SPACEBAR to close this program. Be sure to notify the experimenter that you have concluded this study.'
    
    instructions.setPos([0, 100])

    if token==0:
        instructions.setText(pre_exp)
    elif token==1:
        instructions.setText(rating)
    else:
    	instructions.setText(goodbye)

    instructions.draw()
    token += 1
    win.flip()

    resume=event.waitKeys(keyList=['space', 'escape'])
    if resume[0][0]=='escape':
        win.close()
        core.quit()

    return token

def gen_order(pairwise): # no 2 consecutive trials can be from the same set

	ult = 'match'
	penult = 'match'

	while ult == penult:

		pair_copy = copy.copy(pairwise)
		order = []
		redundancy = ' '

		for item in range(len(pair_copy)):

			pair = random.choice(pair_copy)

			while pair[0] == redundancy and len(pair_copy) > 1:
				pair = random.choice(pair_copy)

			order.append(pair)
			pair_copy.remove(pair)
			redundancy = pair[0]

		ult = order[-1][0]
		penult = order[-2][0]

	return order

# def pre_exp(win, pair, text, text_two, text_three, box, box_two):

# 	xs = [-350, 350]
# 	random.shuffle(xs)

# 	# draw instructions
# 	text_three.setPos([0, 350])
# 	text_three.setText('Take a moment to compare these two sentences and get a sense of how similar they are. Push the spacebar to continue.')

# 	# draw box and sentence for base
# 	box.setPos([xs[0], 0])
# 	text.setPos([xs[0], 0])
# 	text.setText(pair[0])

# 	# draw box and sentence for target
# 	box_two.setPos([xs[1], 0])
# 	text_two.setPos([xs[1], 0])
# 	text_two.setText(pair[1][0])

# 	box.draw()
# 	box_two.draw()
# 	text.draw()
# 	text_two.draw()
# 	text_three.draw()

# 	win.flip()

# 	resume=event.waitKeys(keyList=['space', 'escape'])
# 	if resume[0][0]=='escape':
# 		win.close()
# 		core.quit()


def compare(win, pair, text, text_two, text_three, box, box_two, timer, scale):

	xs = [-350, 350]
	random.shuffle(xs)

	align = {-350:'Left', 350:'Right'}
	base_position = align[xs[0]]

	# draw instructions
	text_three.setPos([0, 350])
	text_three.setText('Use the slider below to indicate how similar the two sentences are.')

	# draw box and sentence for base
	box.setPos([xs[0], 0])
	text.setPos([xs[0], 0])
	text.setText(pair[0])

	# draw box and sentence for target
	box_two.setPos([xs[1], 0])
	text_two.setPos([xs[1], 0])
	text_two.setText(pair[1][0])

	scale.reset()
	timer.reset()

	# draw scale and wait for response
	while scale.noResponse:

		box.draw()
		box_two.draw()
		text.draw()
		text_two.draw()
		text_three.draw()
		scale.draw()
		win.flip()

		if event.getKeys(keyList='escape'):
			win.close()
			core.quit()

	rt = timer.getTime()
	core.wait(0.5)

	return [base_position, scale.getRating(), rt]





