from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

running           = True
camera            = PiCamera()
camera.resolution = (640, 480)
camera.framerate  = 32
rawCapture        = PiRGBArray(camera, size=(640, 480))
faceCascade       = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while running:
    # give the camera a bit of time to get running
    time.sleep(0.2)

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 200, 0), 2)

        cv2.imshow("Live Feed", image)
        key = cv2.waitKey(1) & 0xFF

        rawCapture.truncate(0)

        if key == ord("q"):
            running = False
            break

cv2.destroyAllWindows()