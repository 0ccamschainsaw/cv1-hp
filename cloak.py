import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#capture background
background = 0
for i in range(30):
    ret, background= cap.read()
    if ret == False:
        continue
   

background = np.flip(background, axis=1)

while True:
    ret, frame = cap.read()
    frame = np.flip(frame, axis = 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    #blur = cv2.GaussianBlur(frame, (35,35), 0)
    lower_g = np.array([30,90,70])
    upper_g = np.array([90,255,255])
    mask1 = cv2.inRange(hsv, lower_g, upper_g)
    cloak = cv2.bitwise_and(background, background, mask = mask1)
    
    inv_mask = cv2.bitwise_not(mask1)
    background2 = cv2.bitwise_and(frame, frame, mask= inv_mask)

    output = cv2.addWeighted(cloak, 1, background2, 1, 0)                    #also cv2.add can be used 

    cv2.imshow('test', output)
    if cv2.waitKey(1) == ord('q'):       
        break    

cap.release()
cv2.destroyAllWindows()

#cloak: bitwise and with background where mask1 is true, that is where color green exists
#background2: original background everywhere except green areas(inv_mask)
#output is then combining both cloak and background2