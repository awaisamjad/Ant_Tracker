import cv2

cap = cv2.VideoCapture("ants_against_white.mp4")

#object_detector = cv2.createBackgroundSubtractorKNN()
object_detector = cv2.createBackgroundSubtractorMOG2() # use  MOG2 Background Subtractor for detecting ants


while True:
    ret, frame = cap.read()
    mask = object_detector.apply(frame)
    countours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    coordinates = []
    for cnt in countours:
        #print(cnt)
        coordinates.append(cnt)
        area = cv2.contourArea(cnt)
        if area > 10 and area < 100: # for the objects detected only take the ones of size > 10 and <100 
            cv2.drawContours(frame, [cnt], -1, (0,255,0), 2)
    
            
    
    cv2.imshow("Frame", frame)
    #cv2.imshow("Mask", mask)
    
    key = cv2.waitKey(30)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()


