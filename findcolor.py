import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Creating track bar
cv2.createTrackbar('H Lower', 'result',0,179,nothing)
cv2.createTrackbar('H Upper', 'result',0,179,nothing)
cv2.createTrackbar('S Lower', 'result',0,255,nothing)
cv2.createTrackbar('S Upper', 'result',0,255,nothing)
cv2.createTrackbar('V Lower', 'result',0,255,nothing)
cv2.createTrackbar('V Upper', 'result',0,255,nothing)

cv2.setTrackbarPos('H Lower', 'result',0)
cv2.setTrackbarPos('H Upper', 'result',179)
cv2.setTrackbarPos('S Lower', 'result',0)
cv2.setTrackbarPos('S Upper', 'result',255)
cv2.setTrackbarPos('V Lower', 'result',0)
cv2.setTrackbarPos('V Upper', 'result',255)

while(1):

    _, frame = cap.read()

    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    hl = cv2.getTrackbarPos('H Lower','result')
    hu = cv2.getTrackbarPos('H Upper','result')
    sl = cv2.getTrackbarPos('S Lower','result')
    su = cv2.getTrackbarPos('S Upper','result')
    vl = cv2.getTrackbarPos('V Lower','result')
    vu = cv2.getTrackbarPos('V Upper','result')

    # Normal masking algorithm
    lower = np.array([hl,sl,vl])
    upper = np.array([hu,su,vu])

    mask = cv2.inRange(hsv,lower, upper)

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()
