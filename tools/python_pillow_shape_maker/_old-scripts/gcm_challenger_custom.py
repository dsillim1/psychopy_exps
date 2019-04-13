 ## Python Standard Library
import sys
import os



## External Dependencies
from PIL import Image, ImageDraw
# import AppKit
import numpy as np

# get screen information; get resolution
# x = [(screen.frame().size.width, screen.frame().size.height)
#     for screen in AppKit.NSScreen.screens()]
# print(x)

#mwetzels macbook
mac = 1280/28.6

#lab monitors
lab_monitor = 1440/41



xdimc = 12
ydimc = 6

# get rectangle size
sizes = np.linspace(2.5,7.1,xdimc) # correct mds
shades = np.linspace(25,230,ydimc) # correct mds


old_dims = np.array([
    [1, 1],
    [3, 4],
    [9, 6],
    [11, 6],

    [3, 1],
    [6, 3],
    [11, 4],

    [6, 6],
    [6, 4],
    [9, 4],
    ], dtype=float)

xlim = 11
ylim = 6

dims = np.copy(old_dims)
# get correct dims
dims[:,0] = ( (dims[:,0] / xlim) * (230 - 25) ) + 25
dims[:,1] = ( (dims[:,1] / ylim) * (7.1 - 2.5) ) + 2.5



print(dims)

# settings
folder = 'images_appear_here'
save = True
res_w = lab_monitor

# essentially deterimes the distribution of items
cluster_values = [.05, 0, .05]

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
            print(folder + os.path.sep + str(int(old_dims[i,0])) + '-' + str(int(old_dims[i,1])) + '.png')
            im.save(folder + os.path.sep + str(int(old_dims[i,0])) + '-' + str(int(old_dims[i,1])) + '.png')
            select_count += 1


