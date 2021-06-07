from MediaPipeTools import TrackHandModule
import cv2


cap = cv2.VideoCapture(0)
hand = TrackHandModule.HandTrack(max_num_hands=1)


while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,  1)
    hand.find_hand(frame)
    lmlist = hand.findPosition(frame)
    if len(lmlist) != 0:
        x1, y1 = int(lmlist[8][1]), int(lmlist[8][2])
        x2, y2 = int(lmlist[4][1]), int(lmlist[4][2])
        
        
        cv2.circle(frame, (int(lmlist[8][1]), int(lmlist[8][2])),  10, (255, 0, 0), cv2.FILLED)
        cv2.circle(frame, (int(lmlist[4][1]), int(lmlist[4][2])), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(frame, (cx, cy), 6, (255, 0, 0), cv2.FILLED)

        
    cv2.imshow("Controller", frame)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break 
cap.release()
cv2.destroyAllWindows()
