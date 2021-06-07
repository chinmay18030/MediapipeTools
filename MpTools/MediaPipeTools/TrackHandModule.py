import cv2
import mediapipe as mp

# Used for tracking hands
# Use static_image_hands is eual to true if finding hands in a image
class HandTrack:
    def __init__(self,
                 static_image_mode=False,
                 max_num_hands=2,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5
                 ):
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.mpDraw = mp.solutions.drawing_utils
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.static_image_mode,
                                        self.max_num_hands,
                                        self.min_detection_confidence,
                                        self.min_tracking_confidence)
    # this function draws the hand landmarks on a image or photo

    def find_hand(self, mat, draw=True, connections=True):
        rgb = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        if draw:
            if results.multi_hand_landmarks:
                for handlm in results.multi_hand_landmarks:
                    if connections:
                        self.mpDraw.draw_landmarks(mat, handlm, self.mpHands.HAND_CONNECTIONS)
                    if not connections:
                        self.mpDraw.draw_landmarks(mat, handlm)
        return mat
    # find position helps to find exact x an y location of a hand landmark. It returns a list of all the coordinates

    def findPosition(self, img, handNo=0, draw=True):
        lmlist =[]
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        if results.multi_hand_landmarks:
            myHands = results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHands.landmark):
                h,w,c = img.shape
                cx, cy = (lm.x*w),(lm.y*h)
                lmlist.append([id,cx,cy])
        return lmlist


