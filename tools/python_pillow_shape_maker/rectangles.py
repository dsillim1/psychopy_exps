 ## Python Standard Library
import sys
import os



## External Dependencies
from PIL import Image, ImageDraw
# import AppKit
import numpy as np

import pandas as pd

# get screen information; get resolution
# x = [(screen.frame().size.width, screen.frame().size.height)
#     for screen in AppKit.NSScreen.screens()]
# print(x)

#mwetzels macbook
mac = 1280/28.6

#lab monitors
lab_monitor = 1440/41



xdimc = 9
ydimc = 9

# get rectangle size
# sizes = np.linspace(2.5,7.1,xdimc) # correct mds
# shades = np.linspace(25,230,ydimc) # correct mds


old_dims = np.array(
    [
        [3, 2], # As
        [3, 3],
        [3, 4],
        [4, 3],
        [4, 4],
        [5, 4],
        [2, 1], # new As, control
        [2, 2],
        [2, 3],
        [2, 4],
        [3, 5], # new As, exp
        [4, 5],
        [5, 5],
        [6, 5],

        [2, 9], # Bs
        [3, 7],
        [4, 8],
        [4, 9],
        [5, 7],
        [6, 9],

        [5, 1], # Cs
        [6, 1],
        [6, 2],
        [7, 1],
        [7, 2],
        [7, 3],
        [8, 1],
        [8, 2],
        [8, 3],
        [8, 4],

        [3, 1], # GAs
        [4, 2],
        [5, 3],
        [6, 4],
        [7, 5],
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 5],
        [4, 1], # GCs
        [5, 2],
        [6, 3],
        [7, 4],
        [8, 5], 
        [1, 6], # UL
        [2, 6],
        [3, 6],
        [4, 6],
        [5, 6],
        [6, 6], # UR
        [7, 6],
        [8, 6],
    ], 
    dtype=float
)


import matplotlib.pyplot as plt 
plt.scatter(old_dims[:,0], old_dims[:,1])
plt.show()





xlim = 10
ylim = 10

dims = np.copy(old_dims)
# get correct dims
dims[:,0] = ( (dims[:,0] / xlim) * (230 - 25) ) + 25
dims[:,1] = ( (dims[:,1] / ylim) * (7.1 - 2.5) ) + 2.5



print '\n',dims


sys.exit()
# settings
folder = 'images_appear_here'
save = True
res_w = lab_monitor

# essentially deterimes the distribution of items
# cluster_values = [.05, 0, .05]

As = ['A_']*14
Bs = ['B_']*6
Cs = ['C_']*10

GAs = ['GA_']*11
GCs = ['GC_']*5

ULs = ['UL_']*5 # upper left
URs = ['UR_']*3

letters = As + Bs + Cs + GAs + GBs + GCs + ULs + URs + BRs

temp_dict = {'item_type':letters}

frame = pd.DataFrame(temp_dict)


##_Run Stim Generation
item_count = 1
select_count = 1
if save == True:
    for i in range(dims.shape[0]):
        # print((i) % 3)

            #get stim dimensions
            # d = dims[i,0] * res_w
            # s = int(np.round(dims[i,1]))

            d = dims[i,1] * res_w
            s = int(np.round(dims[i,0]))


            # size of image
            v=650
            canvas = (v,v)


            # something for saving it (idk i didn't write these next parts)
            thumb = canvas[0], canvas[1]


            # init canvas
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)

            # draw rectangles
            x1 = canvas[0]/2 - d/2
            y1 = canvas[0]/2 + d/2
            x2 = canvas[0]/2 + d/2
            y2 = canvas[0]/2 - d/2

            draw.rectangle([x1, y1, x2, y2],
                outline = (0, 0, 0, 255), 
                fill = (s,s,s,255))

            # make thumbnail
            im.thumbnail(thumb)


            # save image
            if not os.path.exists(folder):
                os.makedirs(folder)
            print(folder + os.path.sep + frame.iat[i,0] + str(int(old_dims[i,0])) + '-' + str(int(old_dims[i,1])) + '.png')
            im.save(folder + os.path.sep + frame.iat[i,0] +  str(int(old_dims[i,0])) + '-' + str(int(old_dims[i,1])) + '.png')
            select_count += 1


