# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#!/usr/bin/env python

import numpy as np
import cv2
import time
import draw_sprites
from collections import deque
from PIL import Image, ImageTk
import Tkinter as tk

global frame
def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=2, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    pil_im = Image.fromarray(np.uint8(cm.gist_earth(img)*255))
    faces=[]
    for x1, y1, x2, y2 in rects:
        faces.append([[(x1+x2)/2,(y1+y2)/2]])
    pil_img=draw_sprites.draw_sprites(pi,faces)
    img=image2array(pil_img)


def quit_(root):
    root.destroy()


def update_fps(fps_label):
    frame_times = fps_label._frame_times
    frame_times.rotate()
    frame_times[0] = time.time()
    sum_of_deltas = frame_times[0] - frame_times[-1]
    count_of_deltas = len(frame_times) - 1
    try:
        fps = int(float(count_of_deltas) / sum_of_deltas)
    except ZeroDivisionError:
        fps = 0
    fps_label.configure(text='FPS: {}'.format(fps))


def update_all(root, canvas, cam, fps_label):
    #update_image(canvas, cam)
    
    ret, img = cam.read()
    cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    rects = detect(gray, cascade)
    vis = img.copy()
    vis = vis[...,::-1]#converts BGR to RGB
    a = Image.fromarray(vis)
    
    faces=[]
    for x1, y1, x2, y2 in rects:
        faces.append([[(x1+x2)/2,(y1+y2)/2]])
    draw_sprites.draw_sprites(a,faces)
        
    b = ImageTk.PhotoImage(image=a)
    #canvas.delete(tk.ALL)
    #canvas.delete('all')
    global frame 
    frame = canvas.create_image(0,0,image=b,anchor=tk.NW) 
    root.update()
    time.sleep(.001)
    update_fps(fps_label)
    root.after(0, func=lambda: update_all(root, canvas, cam, fps_label))
    
    
if __name__ == '__main__':
    import sys, getopt
    
    cascade_fn='haarcascades/haarcascade_frontalface_alt.xml'

    cascade = cv2.CascadeClassifier(cascade_fn)

    cam = cv2.VideoCapture(0)
    root = tk.Tk() 
    
    #image_label = tk.Label(master=root)# label for the video frame
    #image_label.pack()
    
    
    videoframe = tk.LabelFrame(root,text='Captured video')
    videoframe.grid(column=0,row=0,columnspan=1,rowspan=1,padx=5, pady=5, ipadx=5, ipady=5)
    canvas = tk.Canvas(videoframe, width=640,height=480)
    canvas.grid(column=0,row=0)
    Im = Image.open("test.jpg")
    b = ImageTk.PhotoImage(Im) 
    fps_label = tk.Label(master=videoframe)# label for fps
    fps_label._frame_times = deque([0]*5)  # arbitrary 5 frame average FPS
    fps_label.grid(column=0,row=1)
    quit_button = tk.Button(master=videoframe, text='Quit',command=lambda: quit_(root))
    quit_button.grid(column=0,row=2)
    # setup the update callback
    root.after(0, func=lambda: update_all(root, canvas, cam, fps_label))
    root.mainloop()
    del cam

# <codecell>


# <codecell>


# <codecell>


# <codecell>


