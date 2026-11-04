from picamera import PiCamera
camera = PiCamera()
camera.capture('/tmp/test.jpg')
camera.close()
print("Done")