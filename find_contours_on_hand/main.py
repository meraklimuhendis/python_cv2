import cv2 
import imutils




"""
Kontür Belirleme Algoritması:
Bu algoritma ile resimde bulunan cisimlerin şekillerinin algılanması amaçlanmıştır.

Yapılacak aşamalar;
1. Resim gri tona çekilir.
2. Blur atılır.
3. Resmin verilen parametler ile tresholdu belirlenir.
4. Erode işlemine sokularak resimde ufak tefek kalan gereksiz işaretlemeler yok edilmiş olur.
5. Dilate işlemine sokularak kalan belirgin kenarlar daha da belirginleştirilir.
6. Resmin son halindeki konturler tespit edilir. Ve kontürler istenen renkte çizilir.
"""


image_file_path     = "hand.jpeg"
image               = cv2.imread(image_file_path)

# Orginal Image
cv2.imshow('Orginal Image', image) 
cv2.waitKey(0)

gray_tone   = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Direk binary ile çevrilebilir.
blur_image  = cv2.GaussianBlur(gray_tone, (5, 5), 0)
# Tresh, erode, dilate
thresh      = cv2.threshold(blur_image, 45, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('Thresh', thresh)
cv2.waitKey(0)
erode      = cv2.erode(thresh, None, iterations=2)
cv2.imshow('Erode', erode)
cv2.waitKey(0)
dilate      = cv2.dilate(erode, None, iterations=2)
cv2.imshow('Dilate', dilate)
cv2.waitKey(0)
# Contours
# Bu kısımda kontur belirlenir;
cnts        = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts        = imutils.grab_contours(cnts)
contours    = max(cnts, key=cv2.contourArea)
cv2.drawContours(image, [contours], -1, (0, 0, 255), 2)

# Resimde son kalan tüm şekillere kontur atar;
# Örnek olması için bıraktım;
# cv2.drawContours(image, cnts[0], -1, (0, 0, 255), 2)

cv2.imshow('With Countours', image)
cv2.waitKey(0)


# Save
cv2.imwrite("contour_hand.jpeg", image)