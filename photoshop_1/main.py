import cv2
import matplotlib.pyplot as plt
import numpy as np




image_file_path     = "dog_4.jpeg" # Ufak köpek
image_file_path_2   = "dog.jpeg"   # Büyük köpek
image               = cv2.imread(image_file_path)
image_2             = cv2.imread(image_file_path_2)

# cv2.imshow('Dog', image_2)
# cv2.waitKey(0)

## Yapıştırılacak resmin boyutları küçültülecek;
image = cv2.resize(image, (int(image.shape[1] * 30 / 100), int(image.shape[0] * 30 / 100)))
# print(image.shape)
cv2.imshow('image_2', image_2)
cv2.waitKey(0)
## Yapıştırılacak resmin boyutu kadar ana fotoğraftan boyut alınacak;
image_2_crop = image_2[310:310 + image.shape[0], 480:480 + image.shape[1]]
cv2.imshow('image_2_crop', image_2_crop)
cv2.waitKey(0)


# Yapıştırılacak resmin içinden köpek dışındaki alanlar temizlenecek;
image_gray      = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, mask       = cv2.threshold(image_gray, 232, 255, cv2.THRESH_BINARY)
mask_inv        = cv2.bitwise_not(mask) # Mask taki görüntü değerlerini tersler;
im1_bg          = cv2.bitwise_and(image, image, mask = mask_inv) # ters olan görüntü değerleri ile and işlemine sokar;
im2_fg          = cv2.bitwise_and(image_2_crop, image_2_crop, mask = mask)
last_image_crop = cv2.add(im1_bg, im2_fg)
cv2.imshow('image_2_crop', last_image_crop)
cv2.waitKey(0)

# Kesilen ve temizlenen kısım ana fotoğrafa tekrar yerleştirilecek;
image_2[310:310 + image.shape[0], 480:480 + image.shape[1]] = last_image_crop
cv2.imshow('image_2', image_2)
cv2.waitKey(0)

# Save
cv2.imwrite("new_dog.jpeg", image_2)