#Header
#Matthew Baker
#Evergreens
#Dr. Melissa Collins
#Engineering 1050
#November 4, 2026
#Image Processing
#Problem: Create a image processing function
#Solution: Have the robot look for a picture and manipulate it


#Imports
from picamera import PiCamera

from picamera.array import PiRGBArray

import cv2

import time
#import sphero_sdk

time.sleep(2)
print("sleep", flush = True)

#take pic
camera = PiCamera()
print("camera_activate", flush = True)
raw_capture = PiRGBArray(camera)
print("capture", flush = True)
time.sleep(0.1)
print("sleep 2 eletric boogaloo", flush = True)
camera.capture(raw_capture, format="bgr")
print("camera_capture", flush = True)
image = raw_capture.array
print("image", flush = True)

#grayscale pic
#img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#print("gray", flush = True)
#resize pic
#img_resized = cv2.resize(img_gray, None, fx = 0.5, fy = 0.5)
#print("resize", flush = True)
#rotate pic
#img_rotate = cv2.rotate(img_resized, cv2.ROTATE_90_CLOCKWISE)
#print("rotate", flush = True)
#Download to computer
cv2.imwrite('/tmp/eg_rvr_final_img.jpg', image)
camera.close()
def getDominantColor():
    camera = PiCamera()
    raw_capture = PiRGBArray(camera)
    time.sleep(0.1)
    camera.capture(raw_capture, format="bgr")
    image = raw_capture.array
    blue, green, red = image.mean(axis=(0,1))
    print(f"Red: {red:.1f}")
    print(f"Green: {green:.1f}")
    print(f"Blue: {blue:.1f}")
    camera.close()
    if red > blue and red > green:
        return "Red"
    elif blue > red and blue > green:
        return "Blue"
    elif green > red and green >blue:
        return "Green"
    else:
        return "Bad Reading"

    return None
color = getDominantColor()
print("Dominant color =", color)
print("Done")