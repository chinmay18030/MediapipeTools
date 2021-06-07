import cv2
import mediapipe as mp

# Meshface helps to find all the facial landmarks
# Use static image = True is using a photo
class MeshFace:
    def __init__(self,
                 static_image_mode=False,
                 max_num_faces=1,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5
                 ):
        self.static_image_mode = static_image_mode
        self.max_num_faces = max_num_faces
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFace = mp.solutions.face_mesh
        self.mesh = self.mpFace.FaceMesh(self.static_image_mode,
                                         self.max_num_faces,
                                         self.min_detection_confidence,
                                         self.min_tracking_confidence)

    # TO draw the facial landmarks
    def find_face(self, mat, draw=True, connections=True):
        rgb = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)
        self.results = self.mesh.process(rgb)
        if draw:
            if self.results.multi_face_landmarks:
                for handlm in self.results.multi_face_landmarks:
                    if connections:
                        self.mpDraw.draw_landmarks(mat, handlm, self.mpFace.FACE_CONNECTIONS)
                    elif not connections:
                        self.mpDraw.draw_landmarks(mat, handlm)
        return mat

    # returns a list with x and y position of each landmark
    def findPosition(self, frame, handNo=0):
        lmlist = []
        if self.results.multi_face_landmarks:
            for handlm in self.results.multi_face_landmarks:
                myhands = self.results.multi_face_landmarks[handNo]
                for id, lm in enumerate(myhands.landmark):
                    h, w, c = frame.shape
                    cx, cy = (lm.x*w), (lm.y*h)
                    lmlist.append([id, cx, cy])
        return lmlist
