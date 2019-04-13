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






# get rectangle size
# sizes = np.linspace(2.5,7.1,15) # correct mds
# shades = np.linspace(25,230,15) # correct mds
sizes = np.linspace(.5,13,9)
shades = np.linspace(10,245,9)

sizes_exp = np.exp(sizes)
sizes_exp_scaled = sizes / sizes.max() 
sizes = sizes * sizes_exp_scaled
shades_exp = np.exp(shades)
shades_exp_scaled = shades / shades.max() 
shades = shades * shades_exp_scaled

#make combination set
combs = []
for size, shade in zip(sizes, shades):
    combs.append([size,shade])

dims = np.array(combs)
print(dims)


# settings
folder = 'images_appear_here'
save = True
res_w = lab_monitor


##_Run Stim Generation
item_count = 1
select_count = 1
if save == True:
    for i in range(dims.shape[0]):

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
        x1 = canvas[0]/2 - d/2 - (d/2)
        y1 = canvas[0]/2 + d/2 + (d/2)
        x2 = canvas[0]/2 + d/2 + (d/2)
        y2 = canvas[0]/2 - d/2 - (d/2)

        draw.rectangle([x1, y1, x2, y2],
            outline = (0, 0, 0, 255), 
            fill = (s,s,s,255))
        print(x1,y1)
        print(x2,y1)

        # make thumbnail
        im.thumbnail(thumb)


        # save image
        if not os.path.exists(folder):
            os.makedirs(folder)
        im.save(folder + '/' + str(select_count)+'.png')
        select_count += 1






