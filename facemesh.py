#Face Mesh Module 

from MediaPipeTools import MeshFaceModule
import cv2


cap = cv2.VideoCapture(0)
mesh = MeshFaceModule.MeshFace()


while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,  1)
    mesh.find_face(frame)
    

        
    cv2.imshow("Face Mesh Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break 
cap.release()
cv2.destroyAllWindows()
