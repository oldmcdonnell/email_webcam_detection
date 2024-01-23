import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1) # wait for video to process

while True:
    check, frame = video.read() # reads vide
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    cv2.imshow("My Video", gray_frame_gau) # sends data to visual file

    key = cv2.waitKey(1) #keyboard key object

    if key == ord("q"): #break if use presses q
        break

video.release()