# Mediapipetools
MediaPipeTools is a mediapipe helper package which helps  you to track hands landmarks, face landmarks and full body landmarks. This package makes your work very easy. To install use 
```bash
pip install MediaPipeTools
```
Versions available
+  `0.11`
+  `0.12`

## Use
MediaPipeTools give three tools for now
+ TrackHandModule
+ PoseTrackModule
+ MeshFaceModule

## TrackHandModule
```python
from MediaPipeTools import TrackHandModule
# Here we are using the live webcam
cap = cv2.VideoCapture(0)
#This is the track hand module class
hand = TrackHandModule.HandTrack(max_num_hands=1,static_image_mode = False)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    #This command draws the landmarks on the hand if any visible in the frame
    hand.find_hand(frame)
    # This returns a list having the coordiantes of each landmark
    lmlist = hand.findPosition(frame)
    if len(lmlist) != 0:
        x1, y1 = int(lmlist[8][1]), int(lmlist[8][2])
        x2, y2 = int(lmlist[4][1]), int(lmlist[4][2])

        cv2.circle(frame, (int(lmlist[8][1]), int(lmlist[8][2])), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(frame, (int(lmlist[4][1]), int(lmlist[4][2])), 10, (255, 0, 0), cv2.FILLED)

    cv2.imshow("Controller", frame)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
cap.release()
cv2.destoryAllWindows()
```
Same Coordinates tracking can be done by each of the modules
For more info, see my github page 
```
https://github.com/chinmay18030/MediapipeTools
```
# Landmarks
Each module detects or track something. But how to find these coordinates.Mediapipe finds the hand and plots the landmarks and gives them an id
###Hand
![image](https://user-images.githubusercontent.com/77487404/120963571-76a17980-c77f-11eb-83ad-cd280cf2607a.png)
### Pose
![image](https://user-images.githubusercontent.com/77487404/120963870-fb8c9300-c77f-11eb-8b26-6da774088527.png)

You see each has an id so we use the id to find that particular landmark
