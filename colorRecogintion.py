#Header
#Matthew Baker
#Evergreens
#Dr. Melissa Collins
#Engineering 1050
#October 27, 2026
#RVR Code First Draft
#Problem: Create a multi-function program with loops and sensors
#Solution: Have the robot look for the color red and if it doesn't see it, move to the next location

#Imports
from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import time
import math

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

cv2.imwrite('/tmp/eg_rvr_color.jpg', image)
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