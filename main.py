import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1) # wait for video to process

while True:
    check, frame = video.read() # reads vide
    cv2.imshow("My Video", frame) # sends data to visual file

    key = cv2.waitKey(1) #keyboard key object

    if key == ord("q"): #break if use presses q
        break

video.release()