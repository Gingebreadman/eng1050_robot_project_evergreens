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
import sys
import time
import math
#import sphero_sdk
sys.path.append('/home/pi/sphero-sdk-raspberrypi-python')
from colorRecognition import getDominantColor #Imports the color detection from colorRecogintion.py

from sphero_sdk import SpheroRvrObserver
rvr = SpheroRvrObserver()

rvr.wake()

# # There a couple of locations for drive commands, the first can simply be found in the Sphero_Sdk library.
# print("\n--- Sphero_Sdk Options---")
# print("Attributes:", dir(sphero_sdk))
# #Commands like wake to wake up your robot, set_all_leds, get_rgbc_sensor_values, and drive_with_heading to name a few you may find useful.
#
#
# # Explore DriveControlAsync
# print("\n--- DriveControlAsync ---")
# print("Attributes:", dir(sphero_sdk.DriveControlAsync))
# #the last half of this line is your different functions you can use (drive_backward_seconds, etc)
#
# # To understand what inputs are required, use the help command
# # Where is says "self" you can ignore if you are using the format of rvr.drive_control.drive_forward_seconds
# # The rvr. at the front is the "self"
# print("\n ---Help with Specific Command---")
# help(sphero_sdk.DriveControlAsync.drive_forward_seconds)



def look_at_pepper(s, t):
    #Purpose: Drive to pepper and look at it
    #Inputs: Pepper Number, color
    #Outputs: If the pepper is red
    #Notes: None
    pepper_number = int(input("How many peppers? "))


    while pepper_number > 0: #While loop to move between peppers
        #Checking pepper color
        color = getDominantColor() #Assigns the function defined in colorRecogintion.py to the variable "color"
        if color == "Red":
            print("Red Pepper found")
            pepper_number -= 1
        elif color == "Green":
            print("Green Pepper found")
            pepper_number -= 1
        else:
                print ("No pepper found")

        #driving between peppers
        rvr.drive_with_rotation(-s,0, t)
        time.sleep(2)
        rvr.drive_with_rotation(s,-90,t)
        time.sleep(2)
        rvr.drive_with_rotation(s,0,t*2.5)
        time.sleep(2)
        rvr.drive_with_rotation(s,90,t)
        time.sleep(2)
        rvr.drive_with_rotation(s,0, t)
        time.sleep(10)

        #With the above block, the robot will back up, turn right, drive straight, then turn left,
        #before driving straight to look at the pepper, no matter how it's oriented

    print("No more peppers") #Print when it runs out of peppers

#This is how we *call* the function and ultimately allow for an interruption and closing of the rvr object

if __name__ == '__main__':
    try:  #thing to try doing that may generate an exemption
        look_at_pepper(60, 2)
    except KeyboardInterrupt:
        print("User ended by pressing Ctrl+C")
    finally:
        #what to do before we exit the block
        rvr.close()