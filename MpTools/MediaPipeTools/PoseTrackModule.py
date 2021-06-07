import cv2, mediapipe as mp


class PoseTrack:
    def __init__(self,
                 static_image_mode=False,
                 upper_body_only=False,
                 smooth_landmarks=True,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5
                 ):
        self.static_image_mode = static_image_mode
        self.upper_body_only = upper_body_only
        self.smooth_landmarks = smooth_landmarks
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.static_image_mode,
                                     self.upper_body_only,
                                     self.smooth_landmarks,
                                     self.min_detection_confidence,
                                     self.min_tracking_confidence)

    def find_pose(self, mat, draw=True, connections=True):
        rgb = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)
        results = self.pose.process(rgb)
        if draw:
            if results.pose_landmarks:
                if connections:
                    self.mpDraw.draw_landmarks(mat, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
                elif not connections:
                    self.mpDraw.draw_landmarks(mat, results.pose_landmars)
        return mat

    def findPosition(self, img, handNo=0, draw=True):
        lmlist =[]
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.pose.process(rgb)
        if results.multi_hand_landmarks:
            mypose = results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(mypose.landmark):
                h,w,c = img.shape
                cx, cy = (lm.x*w),(lm.y*h)
                lmlist.append([id,cx,cy])
        return lmlist
