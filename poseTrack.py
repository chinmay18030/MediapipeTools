import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
cap = cv2.imread("photo/")
cap = cv2.resize(cap, (840, 680))

rgb = cv2.cvtColor(cap,cv2.COLOR_BGR2RGB)
results = pose.process(rgb)

if results.pose_landmarks:

    mp_draw.draw_landmarks(cap,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)
cv2.imshow("MediaPipe Pose Detection", cap)
cv2.waitKey(0)


