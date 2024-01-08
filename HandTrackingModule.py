import cv2 as cv
import mediapipe as mp
import time

class handDetector():

    def __init__(self, mode=False, max_hands=2, model_complexity=1, detection_conf=0.5, tracking_conf=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_conf = detection_conf
        self.tracking_conf = tracking_conf
        self.mpHands = mp.solutions.hands
        self.model_complexity = model_complexity
        self.hands = self.mpHands.Hands(self.mode, self.max_hands, self.model_complexity, self.detection_conf,self.tracking_conf)
        # For extrapolating the connections in the Hand
        self.mpDraw = mp.solutions.drawing_utils






    def findHands(self,frame,draw=True):
        rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        list=[]
        # print(results.multi_hand_landmarks) #gives information(co-ordinates) of each point
        if results.multi_hand_landmarks:
            for handlms in results.multi_hand_landmarks:
                for id, lm in enumerate(handlms.landmark):
                    # print(id,lm) #we want pixel values
                    h, w, c = frame.shape  # height ,width ,channels
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    list.append([id, cx, cy])
                if draw:
                    self.mpDraw.draw_landmarks(frame, handlms, self.mpHands.HAND_CONNECTIONS)
        return frame,list


def main():
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    detector=handDetector()
    while True:
        success, frame = cap.read()
        frame,list =detector.findHands(frame)
        # FPS calculations
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv.putText(frame, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv.imshow("Video", frame)
        if cv.waitKey(1) & 0xFF == ord("d"):
            break

    cap.release()
    cv.destroyAllWindows()




if __name__ =="__main__":
    main()