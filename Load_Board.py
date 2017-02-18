from cv2 import *
import cv2
import numpy as np
i=0
# initialize the camera
cam = VideoCapture(1)   # 1 -> index of camera


s, img = cam.read()

if s:    # frame captured without any errors
    imwrite("emptyBoard.jpg",img) #save image

img_rgb = cv2.imread('emptyBoard.jpg')
cv2.imshow('Detected',img_rgb)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('edge_marker.jpg',0)
w, h = template.shape[::-1]

edges = cv2.Canny(img_gray, 100, 100)
cv2.imshow('Edges', edges)

res = cv2.matchTemplate(edges, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.5
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    print(pt)
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    i+=1
    if i==4:
        break;



cv2.imshow('Detected',img_rgb)

while 1:
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cv2.release()
