# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import time
import cv2
import cv2.cv as cv
 
 
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
 
 
def demo(img):
    print ">>> Loading image..."
    img_color = img
    img_gray = cv2.cvtColor(img_color, cv.CV_RGB2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    #print in_fn, img_gray.shape
 
    print ">>> Detecting faces..."
    start = time.time()
    rects = detect(img_gray)
    end = time.time()
    print 'time:', end - start
    img_out = img_color.copy()
    draw_rects(img_out, rects, (0, 255, 0))
    return img_out
 
def main():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret,img = cap.read()
        image = demo(img)
        cv2.imshow("lll",img)
        k = cv.WaitKey(10);
        if k == 'f':
            break
 
 
if __name__ == '__main__':
    main()

# <codecell>


# <codecell>

#!/usr/bin/env python

import numpy as np
import cv2
import time

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=2, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        
def draw_str(dst, (x, y), s):
    cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2)
    cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255))


if __name__ == '__main__':
    import sys, getopt
    
    cascade_fn='haarcascades/haarcascade_frontalface_alt.xml'

    cascade = cv2.CascadeClassifier(cascade_fn)

    cam = cv2.VideoCapture(0)

    while cam.isOpened:
        ret, img = cam.read()
        if img is None:
            break
        cv2.flip(img,1)
        cv2.imshow('facedetect', img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        t = time.time()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))
        for x1, y1, x2, y2 in rects:
            roi = gray[y1:y2, x1:x2]
            vis_roi = vis[y1:y2, x1:x2]
        dt = time.time() - t

        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        cv2.imshow('facedetect', vis)

        if 0xFF & cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()

# <codecell>


