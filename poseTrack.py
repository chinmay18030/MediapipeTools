#Pose Track Module 
#Pose track module is a mdeiapipe helping module which helps you to use mediapipe very easily 
from MediaPipeTools import PoseTrackModule
import cv2


cap = cv2.VideoCapture(0)
pose = PoseTrackModule.PoseTrack()


while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,  1)
    pose.find_pose(frame)
    

        
    cv2.imshow("Pose Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break 
cap.release()
cv2.destroyAllWindows()
