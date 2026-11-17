import numpy as np
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

def shapeDetect():
    camera = PiCamera()
    raw_capture = PiRGBArray(camera)
    time.sleep(0.1)
    camera.capture(raw_capture, format="bgr")
    img = raw_capture.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray,127,255,1)

    contours,h = cv2.findContours(thresh,1,2)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
        print (len(approx))
        if len(approx)==3:
            print ("Pepper")
            cv2.drawContours(img,[cnt],0,(0,255,0),-1)
        else:
            print ("No pepper")
            continue

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()