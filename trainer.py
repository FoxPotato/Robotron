#   trainer.py

import cv2
import numpy as np
import arraysocket as arso
import thread

ready = True

def recvframe(address):
    global ready

    frame = arso.startserver(address)
    ready = True

while True:
    frame = arso.startserver('192.168.15.113')

    if ready:
        try:
            thread.start_new_thread(recvframe, ('192.168.15.113'))
            ready = False
        except:
            print("Error: unable to start thread")
    
    cv2.imshow('frame_received', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
