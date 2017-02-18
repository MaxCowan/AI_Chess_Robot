from cv2 import *
import cv2
import numpy as np
import time

class Vision:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    idealCoordsDict = {}
    beforeImage = {}
    trackedCoords = []

    def __init__(self):
        # initialize idea coorinate array
        for i in range(0,8):
            for j in range(0,8):
                self.keyName = self.letters[i]+str(j+1)
                self.idealCoordsDict[self.keyName] = (175 + i*56, 419 - j*56)

        self.getTrackedCoords()



    def funcBeforeImage(self):
        tempkeys = []
        for i in range(0, 8):
            for j in range(0, 8):
                self.keyName = self.letters[i] + str(j + 1)
                self.beforeImage[self.keyName] = 0
        for coord in self.trackedCoords:
            tempx, tempy = coord
            print("     x:", tempx, "\n     y:", tempy)
            for idealkey in self.idealCoordsDict:
                idealx, idealy = self.idealCoordsDict[idealkey]
                print("key:", idealkey, "\nx:", idealx - 30, "<", tempx, "<", idealx + 30, "\ny:", idealy - 30, "<", tempy, "<", idealy + 30)
                if idealx - 30 < tempx < idealx + 30:
                    print("Fits x")
                if idealy - 20 < tempy < idealy + 20:
                    print("Fits y")
                if idealx - 30 < tempx < idealx + 30 and idealy - 30 < tempy < idealy + 30:
                    self.beforeImage[idealkey] = 0
                    tempkeys.append(idealkey)
        for coord in self.beforeImage:
            if coord not in tempkeys:
                self.beforeImage[coord] = 1
                # else:
                #     self.beforeImage[idealkey] = 1
        print(tempkeys)
        print(self.beforeImage)
        print(len(self.beforeImage))





    def getTrackedCoords(self):
        self.trackedCoords = []
        cam = VideoCapture(1)  # 1 -> index of camera

        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
        time.sleep(2)

        s, img = cam.read()


        if s:  # frame captured without any errors
            imwrite("emptyBoard.jpg", img)  # save image

        img_rgb = cv2.imread('emptyBoard.jpg')
        cv2.imshow('Detected', img_rgb)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        template = cv2.imread('edge_marker.jpg', 0)
        w, h = template.shape[::-1]

        edges = cv2.Canny(img_gray, 100, 100)
        cv2.imshow('Edges', edges)

        res = cv2.matchTemplate(edges, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.31
        loc = np.where(res >= threshold)
        cv2.imshow('Detected', img_rgb)

        for pt in zip(*loc[::-1]):
            print(pt)
            self.trackedCoords.append(pt)
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

        cv2.imshow('Detected',img_rgb)
        while 1:
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()

# initialize the camera



