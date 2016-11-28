#   agent.py

import cv2
import numpy as np
import arraysocket as arso
import thread

capture = cv2.VideoCapture(0)
capture.set(3, 200)
capture.set(4, 120)

ready = True

def sendframe(frame, address):
    global ready
    
    arso.startclient(frame, address)
    ready = True

while(True):
    ret, frame = capture.read()

    if ready:
        try:
            thread.start_new_thread(sendframe, (frame, '192.168.15.113'))
            ready = False
        except:
            print("Error: unable to start thread")

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
