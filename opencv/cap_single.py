import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

ret, frame = cap.read()
b = frame[:,:,0]
print(b.shape)

xx, yy = np.mgrid[0:b.shape[0], 0:b.shape[1]]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx,yy,b)

# plt.imshow(b)
# plt.plot(b[360,:])
# plt.plot(b[:,640])
# fig, (ax) = plt.subplot(1,1,1)
# ax.imshow(b)

plt.show()

#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     edges = cv.Canny(gray,100,200)
#     # Display the resulting frame
#     cv.imshow('frame', gray)
#     cv.imshow('edges', edges)
#     if cv.waitKey(1) == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()
