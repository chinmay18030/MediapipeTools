import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)
x = cv2.imread("photo/demog.png")
x = cv2.resize(x,(300,300))

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame,(1400,800))
    frame[0:300, 0:300] = x
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handlm in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handlm, mpHands.HAND_CONNECTIONS)
            cv2.cir
    cv2.imshow("Live Video", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
cap.release()
