from MediaPipeTools import holistic as hlt
import cv2

tracker = hlt.Holistic()
cap = cv2.VideoCapture(0)

while True:
  _,frame = cap.read()
  img = tracker.draw_landmarks(frame)
  cv2.imshow("Hel;",img)
  if cv2.waitKey(1) & 0xFF == ord('d'):
    break
cap.release()
cv2.destroyAllWindows()

