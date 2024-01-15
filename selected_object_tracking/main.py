import cv2
import numpy as np

# Pixabay
# video_path = 'ball_3.mp4'
video_path = 'summer_-_24541 (720p).mp4'
# video_path = 'cows_-_85146 (720p).mp4'
video_capture = cv2.VideoCapture(video_path)
# for i in range(10):
ret, frame = video_capture.read()


# Görüntü üzerinde dikdörtgen şeklinde bir alan seçtirir; Bir alt görüntü oluşturur.
bbox = cv2.selectROI("Object Tracking", frame, False)

roi = frame[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# Görüntünün parlaklığını ölçer;
roi_hist = cv2.calcHist([roi_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# Histogram elde edilir;
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# İteratif optimizasyon
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    # Read a new frame from the video
    ret, frame = video_capture.read()

    if not ret:
        break

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Bir görüntüde istenen bölgeye benzer özelliklere sahip bölgeleri işaretler
    # Continuously Adaptive Mean Shift
    frame_backproj = cv2.calcBackProject([frame_hsv], [0, 1], roi_hist, [0, 180, 0, 256], 1)

    # Yakalanan nesnenin bir sonraki karede yeni konumunu ve boyutunu tahmin eder;
    ret, bbox = cv2.CamShift(frame_backproj, bbox, term_crit)

    # Bu kısım her karede istenilen cismin çerçevesini oluşturacaktır;
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Object Tracking", frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
video_capture.release()
cv2.destroyAllWindows()