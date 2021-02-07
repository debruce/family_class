import numpy as np
import cv2 as cv
from pprint import pprint

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# Create some random colors
color = np.random.randint(0,255,(100,3))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    new_size = (int(frame.shape[1]/2), int(frame.shape[0]/2))
    frame = cv.resize(frame, new_size, interpolation = cv.INTER_AREA)
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow('frame', gray)


    p0 = cv.goodFeaturesToTrack(gray, mask = None, **feature_params)
    clr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    for i in range(p0.shape[0]):
        x = p0[i,0,0]
        y = p0[i,0,1]
        print(f"x={x} y={y}")
        cv.circle(clr, (int(x), int(y)), 5, (0,0,255), -1)
    cv.imshow('clr', clr)

    # edges = cv.Canny(gray,100,200)
    # cv.imshow('edges', edges)

    # clr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    # linesP = cv.HoughLinesP(edges, 1, np.pi / 180, 50, None, 50, 10)
    # if linesP is not None:
    #     for i in range(0, len(linesP)):
    #         l = linesP[i][0]
    #         cv.line(clr, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    # cv.imshow('show Hough lines', clr)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
