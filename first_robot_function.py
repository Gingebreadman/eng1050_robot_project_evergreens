import sys
import time
#import sphero_sdk
sys.path.append('/home/pi/sphero-sdk-raspberrypi-python')

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


def my_square(s, d, t):
    # s = 60 #speed
    # d = 0 #heading
    # t = 2 #time
    for i in range(0, 360, 90):
        rvr.drive_with_heading(s, d+i, t)
        time.sleep(2)
    rvr.drive_with_heading(0, 0, t)





if __name__ == '__main__':
    try:  #thing to try doing that may generate an exemption
        my_square(60, 0, 2)
    except KeyboardInterrupt:
        print("User ended by pressing Ctrl+C")
    finally:
        #what to do before we exit the block
        rvr.close()

