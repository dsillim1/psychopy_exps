bases =[
'John wanted something to drink, so he went downstairs to the vending machine.',
'Lily lost her phone, so she searched her backpack.',
'Carl felt nauseous, so he nibbled on saltines for dinner.',
'Jessica broke her oven, so she hired a repairman.',
'The dog kept barking at the squirrel, so the squirrel ran out of the garden.',
'Amelia was watching a movie, so she did not notice someone at the door.'
]

targets = [
['John had not had his hair done for a while, so he called the salon.'],
['Betty had not had her hair done for a while, so she called the salon.'],
['John wanted a candy bar, so he asked his mom for permission.'],
['Betty was tempted by a candy bar, so she asked her mom for permission.'],
['John wanted a candy bar, so he went to the convenience store.'],
['Betty was tempted by a candy bar, so she biked to the convenience store.'],
['Lily failed to set her alarm, so she had to rush to work.'],
['Mary failed to set her alarm, so she had to rush to work.'],
['Lily lost her car keys, so she rode the bus.'],
['Mary misplaced her car keys, so she rode the bus.'],
['Lily lost her car keys, so she searched her purse.'],
['Mary misplaced her car keys, so she looked through her purse.'],
['Carl was worried about identity theft, so he froze his bank account.'],
['Ellen was worried about identity theft, so she froze her bank account.'],
['Carl felt nauseous, so he scheduled an appointment with his doctor.'],
['Ellen was sick, so she scheduled an appointment with her doctor.'],
['Carl felt sick, so he nibbled on dry toast for dinner.'],
['Ellen was sick, so she ate dry toast for dinner.'],
['Jessica was tired after practice, so she took a nap on her couch.'],
['Ralph was tired after practice, so he took a nap on his couch.'],
['Jessica broke her refrigerator, so she bought a new one.'],
['Ralph damaged his refrigerator, so he bought a new one.'],
['Jessica broke her refrigerator, so she hired an electrician.'],
['Ralph damaged his refrigerator, so he employed an electrician.'],
['The dog rolled around in mud, so its fur got dirty.'],
['The wolf rolled around in mud, so its fur got dirty.'],
['The dog kept barking at the rabbit, so the entire neighborhood woke up.'],
['The wolf kept growling at the rabbit, so the entire neighborhood woke up.'],
['The dog kept barking at the rabbit, so the rabbit ran out of the yard.'],
['The wolf kept growling at the rabbit, so the rabbit scurried out of the yard.'],
['Amelia did not properly fold her laundry, so her clothes were wrinkled.'],
['Cole did not properly fold his laundry, so his clothes were wrinkled.'],
['Amelia was watching a tv show, so she burned her food in the oven.'],
['Cole was viewing a tv show, so he burned his food in the oven.'],
['Amelia was watching a tv show, so she did not notice her phone ring.'],
['Cole was viewing a tv show, so he did not hear his phone ring.']
]

sets = [
targets[0:6],
targets[6:12],
targets[12:18],
targets[18:24],
targets[24:30],
targets[30:36]
]

forms = ['LI','AN'] * 3
matches = ['M0','M0','M1','M1','M2','M2']
setLabels = ['S1','S2','S3','S4','S5','S6']
pairwise = []

for s in sets:

	s_indx = sets.index(s)
	label = setLabels[s_indx]
	base = bases[s_indx]

	for t in s:

		t_indx = s.index(t)
		t += [label, matches[t_indx], forms[t_indx], 0]
		pairwise.append([base, t])
