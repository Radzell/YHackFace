# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os
import sys
import cv2
import numpy as np
def read_images(path, sz=None):
    """Reads the images in a given folder, resizes images on the fly if size is given.

    Args:
        path: Path to a folder with subfolders representing the subjects (persons).
        sz: A tuple with the size Resizes 

    Returns:
        A list [X,y]

            X: The images, which is a Python list of numpy arrays.
            y: The corresponding labels (the unique number of the subject, person) in a Python list.
    """
    c = 0
    X,y = [], []
    for subject_path, dirnames, filenames in os.walk(path):
        for filename in os.listdir(subject_path):
            if  not os.path.isfile(os.path.join(subject_path, filename)):
                continue
            try:
                im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
                # resize to given size (if given)
                if (sz is not None):
                    im = cv2.resize(im, sz)
                X.append(np.asarray(im, dtype=np.uint8))
                y.append(int(filename[0]))
            except IOError, (errno, strerror):
                print "I/O error({0}): {1}".format(errno, strerror)
            except:
                print "Unexpected error:", sys.exc_info()[0]
                raise
            c = (c+1)
    return [X,y]

# <codecell>

def train_model():
    [X,y] = read_images(os.getcwd()+'/training/', sz=(100,100))
    model = cv2.createFisherFaceRecognizer()
    model.train(np.asarray(X), np.asarray(y))
    return model

# <codecell>

import numpy as np
import cv2
import time
import ImageDraw
from collections import deque
from PIL import Image, ImageTk
import Tkinter as tk
import math
import webbrowser

global frame
global model
global buttons
global db
db={1:["https://www.facebook.com/eoswald39"]\
    ,2:["https://github.com/Newbrict","http://www.linkedin.com/pub/dimitar-dimitrov/65/158/837"]\
    ,3:["https://www.facebook.com/colin.l.rice","https://github.com/c00w","http://www.linkedin.com/in/colinlrice"]\
    ,6:["https://www.facebook.com/josh.makinen","https://plus.google.com/+JoshuaMakinen","https://twitter.com/JoshuaMakinen","http://www.linkedin.com/profile/view?id=289942967&trk=nav_responsive_tab_profile","https://github.com/makinj/"]}

def draw_sprite(image, coor, color=0, radius=30, text="",icon=""):
    draw = ImageDraw.Draw(image)
    x0=int(coor[0]-radius)
    x1=int(coor[0]+radius)
    y0=int(coor[1]-radius)
    y1=int(coor[1]+radius)
    if icon:
        image.paste(icon,(x0,y0),mask=icon)
    else:
        if color:
            draw.ellipse((x0,y0,x1,y1),fill=color)
        else:
            draw.ellipse((x0,y0,x1,y1))
        if(text):
            draw.text(coor,text)
    return image
def draw_sprites(image, data):
    for face in data:
        x_main=face[0][0]+(face[0][2]-face[0][0])/2
        y_main=face[0][1]+(face[0][3]-face[0][1])/2       
        radius=max(face[0][2]-face[0][0],face[0][3]-face[0][1])/2
        #image=draw_sprite(image,[x_main,y_main],radius=radius)
        global db
        count=0
        global buttons
        buttons=[]
        
        for sprite in db[face[1]]:
            x_pos=x_main+(radius+30)*math.sin(math.pi*2.0*count/float(len(db[face[1]])))
            y_pos=y_main+(radius+30)*math.cos(math.pi*2.0*count/float(len(db[face[1]])))
            icon=0
            text="?"
            color=(0,0,0)
            if sprite.find("facebook")!=-1:
                text="f"
                color=(0,0,255)
                icon=Image.open("icons/facebook.png")
            elif sprite.find("twitter")!=-1:
                text="t"
                color=(0,172,238)
                icon=Image.open("icons/twitter.png")
            elif sprite.find("google")!=-1:
                text="+"
                color=(255,0,0)
                icon=Image.open("icons/google.png")
            elif sprite.find("github")!=-1:
                text="g"
                color=(128,128,128)
                icon=Image.open("icons/github.png")
            elif sprite.find("linkedin")!=-1:
                text="l"
                color=(0,128,0)
                icon=Image.open("icons/linkedin.png")
            image=draw_sprite(image, [x_pos, y_pos], color=color, text=text,icon=icon)
            buttons.append([[x_pos, y_pos],sprite])
            count+=1
            
    return  image




def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=2, minSize=(50, 50), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def quit_(root):
    cam.release()
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
        roi = gray[y1:y2, x1:x2]
        temp = roi.copy()
        resized = cv2.resize(temp, (100,100))
        cv2.imwrite("broken.jpg",temp)
        global model
        [p_label, p_confidence] = model.predict(resized)
        if(p_confidence>2800):
            #print p_label
            faces.append([[x1,y1,x2,y2],p_label])
        #print p_confidence
        #print x1, y1, x2, y2
    draw_sprites(a,faces)
        
    b = ImageTk.PhotoImage(image=a)
    #canvas.delete(tk.ALL)
    #canvas.delete('all')
    global frame 
    frame = canvas.create_image(0,0,image=b,anchor=tk.NW) 
    root.update()
    time.sleep(.0001)
    update_fps(fps_label)
    root.after(0, func=lambda: update_all(root, canvas, cam, fps_label))
    
def click(event):
    global buttons
    for button in buttons:
        if event.x>button[0][0]-30 and event.x<button[0][0]+30 and event.y>button[0][1]-30 and event.y<button[0][1]+30:
            webbrowser.open(button[1],new=2)
            
if __name__ == '__main__':
    import sys, getopt
    global model
    model = train_model()
    cascade_fn='haarcascades/haarcascade_frontalface_alt.xml'

    cascade = cv2.CascadeClassifier(cascade_fn)

    cam = cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)
    
    
    root = tk.Tk() 
    
    
    videoframe = tk.LabelFrame(root,text='Captured video')
    videoframe.grid(column=0,row=0,columnspan=1,rowspan=1,padx=5, pady=5, ipadx=5, ipady=5)
    canvas = tk.Canvas(videoframe, width=640,height=480)
    canvas.grid(column=0,row=0)
    fps_label = tk.Label(master=videoframe)# label for fps
    fps_label._frame_times = deque([0]*5)  # arbitrary 5 frame average FPS
    fps_label.grid(column=0,row=1)
    quit_button = tk.Button(master=videoframe, text='Quit',command=lambda: quit_(root))
    quit_button.grid(column=0,row=2)
    # setup the update callback
    canvas.bind("<Button-1>", click)
    root.after(0, func=lambda: update_all(root, canvas, cam, fps_label))
    root.mainloop()
    del cam

# <codecell>


