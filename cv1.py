import requests
import cv2
import numpy as np
import imutils
import mediapipe as mp
import time

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

# cap = cv2.VideoCapture(0)
url = "http://10.136.211.120:8080/shot.jpg"
cap = cv2.VideoCapture(url)
pTime = 0
setCountDown = time.time()
frameTimeFlag = False
time_gap = 5.0
tempx23 = 0
tempy23 = 0
tempz23 = 0
tempx24 = 0
tempy24 = 0
tempz24 = 0

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)

    # success, img = cap.read()
    # print(success, img)
    # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img)  # access to the frame
    # print(results.pose_landmarks)

    # Find the coordinates
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            # print(id, lm)  # get landmark here
            # if (id == 23 or id == 24):
            #     #print(id, lm)
            if (id == 23):
                tempx23, tempy23, tempz23 = lm.x, lm.y, lm.z
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    #
    #
    #
    cTime = time.time()
    if frameTimeFlag is False:
        # coordx_org, coordy_org, coordz_org = [tempx23, tempx24], [tempy23, tempy24], [tempz23, tempz24]
        time.sleep(3)
        org = tempy23
        frameTimeFlag = True
        print("CALIBRATE DONE!")

    if frameTimeFlag:
        if (abs(tempy23 - org) < 0.001):
            print("Standinstill")
        else:
            if tempy23 > org:
                print("moving left")
            if (tempy23 < org):
                print("moving right")
        org = tempy23


        # if a < 0.0:
        #     print("RIGHT")py
        # elif a > 0.0:
        #     print("LEFT")

        # print("diff x: ", a)
        # print("deff z: ", c)
        # ben phai be hon, ben trai lon hon, a
        # tien len z am, lui z duong

    time_gap = time.time()

    fps = 1 / (cTime - pTime)  # 1 frame in how many sec
    pTime = cTime

    cv2.putText(img, str(int(fps)), (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
