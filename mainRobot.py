import sys
import time
sys.path.append('/home/pi/sphero-sdk-raspberrypi-python')
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups
from sphero_sdk import RvrStreamingServices
#Initiate (create) an object
rvr = SpheroRvrObserver()
detected_color = None
rvr.wake()
def color_detected_handler(color_detected_data ):
    global detected_color
    myColor = color_detected_data['ColorDetection']
    detected_color = (
        myColor['R'],
        myColor['G'],
        myColor['B'])
def get_single_color():
    global detected_color
# This line adds the sensor handler do NOT change or move outside of the function
    rvr.sensor_control.add_sensor_data_handler(
        service=RvrStreamingServices.color_detection,
        handler=color_detected_handler)
    rvr.enable_color_detection(is_enabled=True)
    detected_color = None
    rvr.sensor_control.start(interval=250)
    while detected_color is None:
        time.sleep(0.1)
    rvr.enable_color_detection(is_enabled=False)
    rvr.sensor_control.stop()
    return (detected_color)
color = get_single_color()
while True:
    rvr.drive_with_heading (30,0,0)
    time.sleep(0.5)
    color = get_single_color()
    print(color)
    if color[0]>150 and color[0]>color[1]*1.5 and color[0] >color[2]*1.5:
        rvr.drive_with_heading(0,0,0)
    rvr.led_control.set_all_leds_rgb(
        red= color[0],
        green=color[1],
        blue =color[2])
    break
if __name__ == "__main__":
    color = get_single_color()
print("returned color:", color) #You can have it print whatever (or nothing) you want here, these are just a couple of examples
print("Red Color Detected:", color[0])
rvr.close()