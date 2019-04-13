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
ydimc = 12 #(was 6)

# get rectangle size
sizes = np.linspace(2.5,7.1,xdimc) # correct mds
shades = np.linspace(25,230,ydimc) # correct mds


combs = []
idxs = []
for i, size in enumerate(sizes):
    for ii, shade in enumerate(shades):
        combs.append([size,shade])
        idxs.append([i+1, ii+1])



[print(comb[0], comb[1][0], comb[1][1]) for comb in enumerate(zip(idxs, combs))]

dims = np.array(combs)
# print(dims)


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
            d = dims[i,0] * res_w
            s = int(np.round(dims[i,1]))
            # print(d,dims[i,0])

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
            im.save(folder + '/' + str(idxs[i][0]) + '-' + str(idxs[i][1]) +'.png')
            select_count += 1






