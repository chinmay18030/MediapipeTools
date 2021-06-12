"""
MediaPipeTools virtual background package.
Add a virtual background. 
Author : chinmay18030
Pypi : AceCodingStudio
"""
from MediaPipeTools import VirtualBackground as vb
vb = vb.VirtualBackground(modelSelection=0)
cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    video = vb.add_VirtualBackground(frame,None)
    cv2.imshow("VB",video)
    if cv2.waitKey(1) & 0xFF == ord('d'):
      break
cap.release()
cv2.destroyAllWindows()
