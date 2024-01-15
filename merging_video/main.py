import cv2




cap_1 = cv2.VideoCapture('1.mp4')
cap_2 = cv2.VideoCapture('2.mp4')
cap_3 = cv2.VideoCapture('3.mp4')

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1280, 720))


# Videonun ilk 30 karesi fotoğraf olacak;
for n in range(30):
    frame_1 = cv2.imread('1.jpeg')
    image   = cv2.resize(frame_1, (1280, 720))
    out.write(image)
    cv2.imshow("Video Kareleri" , frame_1)
    cv2.waitKey(50)

    
# Videonun ikinci 60 karesi 2. video olacak;
for n in range(60):
    ret, frame_2    = cap_1.read()
    image           = cv2.resize(frame_2, (1280, 720))
    out.write(image)
    cv2.imshow("Video Kareleri" , frame_2)
    cv2.waitKey(24)


# Videonun üçüncü 60 karesi 3.video olacak;
for n in range(60):
    ret, frame_3    = cap_2.read()
    image           = cv2.resize(frame_3, (1280, 720))
    out.write(image)
    cv2.imshow("Video Kareleri" , frame_3)
    cv2.waitKey(24)


# Videonun üçüncü 60 karesi 4.video olacak;
for n in range(60):
    ret, frame_4    = cap_3.read()
    image           = cv2.resize(frame_4, (1280, 720))
    out.write(image)
    cv2.imshow("Video Kareleri" , frame_4)
    cv2.waitKey(24)

# Videonun son 30 karesi fotoğraf olacak;
for n in range(30):
    frame_5 = cv2.imread('2.jpeg')
    image   = cv2.resize(frame_5, (1280, 720))
    out.write(image)
    cv2.imshow("Video Kareleri" , frame_5)
    cv2.waitKey(50)


cap_1.release()
cap_2.release()
cap_3.release()
cv2.destroyAllWindows()
out.release()