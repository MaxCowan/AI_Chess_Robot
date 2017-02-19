from cv2 import *
import cv2
import numpy as np
import time

class Vision:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    idealCoordsDict = {}
    beforeImage = {}
    beforeColors = {}
    afterImage = {}
    afterColors = {}
    trackedCoords = []

    def __init__(self):
        # initialize idea coorinate array
        for i in range(0,8):
            for j in range(0,8):
                self.keyName = self.letters[i]+str(j+1)
                self.idealCoordsDict[self.keyName] = (207 + i*56, 474 - j*56)

        self.initializeBoardSet()


    def initializeBoardSet(self):
        for i in range(0,8):
            for j in range(0,8):
                self.keyName = self.letters[i]+str(j+1)
                if j == 0 or j == 1 or j == 6 or j == 7:
                    self.beforeImage[self.keyName] = 1
                else:
                    self.beforeImage[self.keyName] = 0


    def calculateMove(self):
        tempkeys = []
        for i in range(0, 8):
            for j in range(0, 8):
                self.keyName = self.letters[i] + str(j + 1)
                self.afterImage[self.keyName] = 0
        self.getTrackedCoords()
        for coord in self.trackedCoords:
            tempx, tempy = coord
            #print("     x:", tempx, "\n     y:", tempy)
            for idealkey in self.idealCoordsDict:
                idealx, idealy = self.idealCoordsDict[idealkey]
                # print("key:", idealkey, "\nx:", idealx - 30, "<", tempx, "<", idealx + 30, "\ny:", idealy - 30, "<", tempy, "<", idealy + 30)
                # if idealx - 30 < tempx < idealx + 30:
                #     print("Fits x")
                # if idealy - 20 < tempy < idealy + 20:
                #     print("Fits y")
                if idealx - 35 < tempx < idealx + 35 and idealy - 35 < tempy < idealy + 35:
                    self.afterImage[idealkey] = 0
                    tempkeys.append(idealkey)
        for coord in self.afterImage:
            if coord not in tempkeys:
                self.afterImage[coord] = 1
                # else:
                #     self.beforeImage[idealkey] = 1
        #print("Tempkeys:", tempkeys)
        #print("Length of tempkeys:", len(set(tempkeys)))
        finalMove = self.compareImages()
        #print(finalMove)
        self.beforeImage = self.afterImage
        self.afterImage = {}

        return finalMove

    def compareImages(self):
        originSquare = ""
        endSquare = ""
        fullstring = ""
        tempBefore = 0
        tempAfter = 0
        piecesRemoved = 0

        for square in self.beforeImage:

            if self.beforeImage[square] == 1:
                #print(self.beforeImage[square])
                tempBefore+=1
            if self.afterImage[square] == 1:
                # print(square)
                tempAfter+=1

        piecesRemoved = tempBefore - tempAfter


        print(self.beforeImage)
        for square in self.beforeImage:
            #still need to take care of castling under the 0 peieces removed if statement
            if piecesRemoved == 0:
                if self.beforeImage[square] == 1 and self.afterImage[square] == 0:
                    originSquare = square
                    print("found 1 xD")
                if self.beforeImage[square] == 0 and self.afterImage[square] == 1:
                    endSquare = square
                    print("found 2 xD")
            if piecesRemoved == 1:
                print("YA FD UP AAAARON")

        fullstring = originSquare+endSquare
        return fullstring

    def getTrackedCoords(self):
        self.trackedCoords = []
        cam = VideoCapture(1)  # 1 -> index of camera

        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
        time.sleep(2)

        s, img = cam.read()


        if s:  # frame captured without any errors
            cv2.imwrite("emptyBoard.jpg", img)  # save image

        img_rgb = cv2.imread('emptyBoard.jpg')
        cv2.imshow('Detected', img_rgb)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        template = cv2.imread('edge_marker.jpg', 0)
        w, h = template.shape[::-1]

        edges = cv2.Canny(img_gray, 100, 100)
        cv2.imshow('Edges', edges)

        res = cv2.matchTemplate(edges, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.33
        loc = np.where(res >= threshold)
       # cv2.imshow('Detected', img_rgb)

        for pt in zip(*loc[::-1]):
            x,y = pt
            if x < 250 and y <500:
                print(pt)
            self.trackedCoords.append(pt)
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

        cv2.imshow('Detected',img_rgb)
        while 1:
            k = cv2.waitKey(5) & 0xFF
            if k == 13:
                break
            if k == 27:
                self.getTrackedCoords()
                break

        cv2.destroyAllWindows()


