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

    return frame

while True:
    frame = arso.startserver('192.168.0.206')

    cv2.imshow('frame_received', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
