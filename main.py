import cv2
from ipro import process_img as pi
video=cv2.VideoCapture(1)

ret=True
while(ret):
    ret,frame=video.read()
    img = pi(frame)
    cv2.imshow('frame',img)
    if cv2.waitKey(7) and 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
