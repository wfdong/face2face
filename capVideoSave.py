import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./tmp/output.avi',fourcc, 20.0, (640,480))
count = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #flip 0 vertically flip, 1 水平翻转horizontally flip, -1 水平垂直翻转,
        #frame = cv2.flip(frame,0)
		
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        name = "./tmp/frames/frame%d.jpg"%count
        cv2.imwrite(name, frame)
        count+=1

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()