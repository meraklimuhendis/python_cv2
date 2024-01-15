import cv2
import numpy as np

cap = cv2.VideoCapture("car_-_2165 (Original).mp4")
# cap = cv2.VideoCapture("roads_-_1952 (720p).mp4")

# Framedeki son karelerden hareketsiz alanları çıkartır
backgroundObject = cv2.createBackgroundSubtractorMOG2(history=2)
kernel = np.ones((3,3),np.uint8)
kernel2 = None


fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1280, 720))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    fgmask = backgroundObject.apply(frame)
    # cv2.imshow("fgmask", fgmask)
    _, fgmask = cv2.threshold(fgmask, 20, 255, cv2.THRESH_BINARY)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    fgmask = cv2.dilate(fgmask,kernel2 , iterations=6)
    # cv2.imshow("fgmask_2", fgmask)


    # Konturlar tespit edilecek;
    countors, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    frameCopy = frame.copy()

    # İstenen kontür üstü var mı diye tespit edilecek
    for cnt in countors:
        # if cv2.contourArea(cnt) > 20000:
        if cv2.contourArea(cnt) > 5000:

            # Kontur çerçeve noktaları hesaplanacak;
            x , y, width , height = cv2.boundingRect(cnt)
            cv2.rectangle(frameCopy, (x,y), (x+width, y+ height) , (0,0,255), 2)
            cv2.putText(frameCopy, "Car detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1 , (0,255,0), 2, cv2.LINE_AA)

    # frame'leri mask'larına göre and işlemine sokar.
    forground = cv2.bitwise_and(frame, frame, mask = fgmask)

    # Videolar yatay olarak aynı çerçeveye alınır
    stacked = np.hstack((frame, forground, frameCopy))
    cv2.imshow("stacked", cv2.resize(stacked, None, fx=0.4, fy=0.4))

    # cv2.imshow("forground", forground)
    # cv2.imshow("frameCopy", frameCopy)
    image = cv2.resize(frameCopy, (1280, 720))

    # cv2.imshow("img", image)
    out.write(image)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()