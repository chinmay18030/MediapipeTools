from cv2 iqimport cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)


class PoseDetector:
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

    def find_face(self, mat, draw=True):
        rgb = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)
        results = self.mesh.process(rgb)
        if draw:
            if results.multi_face_landmarks:
                for handlm in results.multi_face_landmarks:
                    self.mpDraw.draw_landmarks(
                        frame, handlm, self.mpFace.FACE_CONNECTIONS)
        return mat


face = PoseDetector()
while True:
    _, frame = cap.read()
    img = face.find_face(frame)
    cv2.imshow("MP face mesh", img)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
cap.release()
cv2.destroyAllWindows()
