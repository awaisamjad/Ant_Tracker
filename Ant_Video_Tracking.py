import cv2

cap = cv2.VideoCapture("ants_against_white.mp4")

#object_detector = cv2.createBackgroundSubtractorKNN()
object_detector = cv2.createBackgroundSubtractorMOG2()


while True:
    ret, frame = cap.read()
    # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # inversion = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # sketch = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # sketch = cv2.medianBlur(sketch,3)
    # canny = cv2.Canny(frame,100,200)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = object_detector.apply(frame)
    countours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    coordinates = []
    for cnt in countours:
        coordinates.append(cnt)
        area = cv2.contourArea(cnt)
        if area > 10 and area < 100:
            cv2.drawContours(frame, [cnt], -1, (0,255,0), 2)
    
            
    
    cv2.imshow("Frame", frame)
    #cv2.imshow("Mask", mask)
    
    key = cv2.waitKey(30)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()


print(coordinates)
# import cv2
# import numpy as np

# cap = cv2.VideoCapture("ants_against_white.mp4")

# #object_detector = cv2.createBackgroundSubtractorKNN()
# object_detector = cv2.createBackgroundSubtractorMOG2()

# # List to store previous positions of ants
# ant_positions = []

# while True:
#     ret, frame = cap.read()
#     # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # inversion = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     # sketch = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # sketch = cv2.medianBlur(sketch,3)
#     # canny = cv2.Canny(frame,100,200)
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     mask = object_detector.apply(frame)
#     countours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
#     for cnt in countours:
#         area = cv2.contourArea(cnt)
#         if area > 10 and area < 100:
#             cv2.drawContours(frame, [cnt], -1, (0,255,0), 2)
            
#             # Find center of current contour
#             M = cv2.moments(cnt)
#             if M["m00"] != 0:
#                 cx = int(M["m10"] / M["m00"])
#                 cy = int(M["m01"] / M["m00"])
                
#                 # Add current position to list of ant positions
#                 ant_positions.append((cx, cy))
                
#                 # Draw line connecting current and previous position of ant
#                 for i in range(len(ant_positions)-1):
#                     cv2.line(frame, ant_positions[i], ant_positions[i+1], (0, 255, 0), 2)
    
#     cv2.imshow("Frame", frame)
#     #cv2.imshow("Mask", mask)
    
#     key = cv2.waitKey(30)
#     if key == 27:
#         break


# cap.release()
# cv2.destroyAllWindows()

