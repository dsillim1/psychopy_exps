from PIL import Image, ImageDraw
# import AppKit
import numpy as np
import os

# get screen information; get resolution
# x = [(screen.frame().size.width, screen.frame().size.height)
#     for screen in AppKit.NSScreen.screens()]
# print(x)

#mwetzels macbook
mac = 1280/28.6

#lab monitors
lab_monitor = 1440/41




#get rectangle size
sizes = np.linspace(1,18,15)


#make combination set
combs = []
for size in sizes:
    combs.append([size])

dims = np.array(combs)
print(dims)


# settings
folder = 'test'
save = True
res_w = lab_monitor

##_Run Stim Generation
if save == True:
    for i in range(dims.shape[0]):

        c_size = 650
        mult = 4
        scale_size = c_size*mult

        #get stim dimensions
        d = dims[i][0] * res_w * mult

        # size of image
        canvas = (scale_size,scale_size)
        # canvas = (c_size,c_size)

        # something for saving it (idk i didn't write these next parts)
        thumb = canvas[0], canvas[1]


        # init canvas
        im = Image.new('RGBA', canvas, (255, 255, 255, 255))
        draw = ImageDraw.Draw(im)

        center = canvas[0]/2


        ## Make Grid
        grey = 180
        width = 3
        w = width/2
        # Outline [[the *2 added to the bottom and right edge are just a PILLOW thing you have to work around, dont have an explanation]]
        draw.line((0+w,0+w,scale_size-w,0+w),fill=(grey,grey,grey,255),width=width)
        draw.line((0+w,0+w,0+w,scale_size-w),fill=(grey,grey,grey,255),width=width)
        draw.line((0+w*2,scale_size-w*2,scale_size-w*2,scale_size-w*2),fill=(grey,grey,grey,255),width=width)
        draw.line((scale_size-w*2,0+w*2,scale_size-w*2,scale_size-w*2),fill=(grey,grey,grey,255),width=width)
        # Verticle Bars
        xspace = np.linspace(0,scale_size,11)
        for x in xspace:
            draw.line((x,0,x,scale_size),fill=(grey,grey,grey,255),width=width)
        yspace = np.linspace(0,scale_size, 11)
        for y in yspace:
            draw.line((0,y,scale_size,y),fill=(grey,grey,grey,255),width=width)


        # get shape dimensions
        x1 = canvas[0]/2 - d/2
        y1 = canvas[0]/2 - d/2
        x2 = canvas[0]/2 + d/2
        y2 = canvas[0]/2 + d/2

        draw.ellipse((x1, y1, x2, y2),
            outline = None, 
            fill = (255,106,0,255))




        im = im.resize((c_size, c_size), Image.ANTIALIAS)

        # make thumbnail
        im.thumbnail(thumb)


        # save image
        if not os.path.exists(folder):
            os.makedirs(folder)
        im.save(folder + '/' + str(i+1)+'.png')





