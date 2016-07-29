import serial
from time import gmtime, strftime
import picamera

ser = serial.Serial('/dev/ttyACM0',9600)
weightdata = ser.readline()
timedata = strftime("%Y-%m-%d %H:%M:%S", gmtime())

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_recording('my_video.h264')
    camera.wait_recording(2)
    camera.stop_recording()

print(weightdata,timedata)