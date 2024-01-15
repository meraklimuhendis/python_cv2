import cv2
import matplotlib.pyplot as plt
import numpy as np




image_file_path     = "building.jpeg"
image               = cv2.imread(image_file_path)

# # Orginal
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.title("Building - Orginal")
# plt.show()


# Orginal
cv2.imshow('Building - Orginal', image)
cv2.waitKey(0)

# Window
window_dimension = [118, 120] # w, h - x, y
image_window = image[210:210 + window_dimension[1], 683:683 + window_dimension[0]]
cv2.imshow('Window', image_window)
cv2.waitKey(0)

# Example 1
# Pencerenin y boyutunun 10'da biri olacak şekilde alınacak;
example_dimension = [118, 12] # w, h - x, y
image_example = image[182:182 + example_dimension[1], 684: 684 + example_dimension[0]]
cv2.imshow('Example', image_example)
cv2.waitKey(0)

# Örnek 1 yapıştırılacak;
for i in range(0, 10):
    image[210 + (i * example_dimension[1]):210 + (i * example_dimension[1]) + example_dimension[1], 683:683 + example_dimension[0]] = image_example
cv2.imshow('Image with Example', image)
cv2.waitKey(0)




# Rotate
y, x            = image.shape[:2]
cx, cy          = (y//2), (x//2)
M               = cv2.getRotationMatrix2D((cx, cx), -2.7, 1.0) # Dönüşüm matrisini hesaplar;
image_rotated   = cv2.warpAffine(image, M, (x, y)) # Dönüşüm matrisi ile fotoğrafı döndürür.
cv2.imshow('Image Rotated', image_rotated)
cv2.waitKey(0)

# Window 2
window_dimension_2 = [100, 125] # w, h - x, y
image_rotated_window_2 = image_rotated[225:225 + window_dimension_2[1], 525:525 + window_dimension_2[0]]
cv2.imshow('Window 2', image_rotated_window_2)
cv2.waitKey(0)

# Example 1
# Pencerenin y boyutunun 10'da biri olacak şekilde alınacak;
example_dimension_2 = [36, 123] # w, h - x, y
image_rotated_example_2 = image_rotated[216:216 + example_dimension_2[1], 620: 620 + example_dimension_2[0]]
cv2.imshow('Example 2', image_rotated_example_2)
cv2.waitKey(0)

# Örnek 2 yapıştırılacak;
for i in range(0, 3):
    image_rotated[225:225 + example_dimension_2[1], 525 + (i * example_dimension_2[0]):525 + (i * example_dimension_2[0]) + example_dimension_2[0]] = image_rotated_example_2
cv2.imshow('Image with Example 2', image_rotated)
cv2.waitKey(0)


# Rotate geri alınacak;
M                   = cv2.getRotationMatrix2D((cx, cx), 2.7, 1.0)
image_rotated_2     = cv2.warpAffine(image_rotated, M, (x, y))
cv2.imshow('Image Rotated 2', image_rotated_2)
cv2.waitKey(0)


## Rotate yapıldığında kenarlarda siyahlıklar kaldığı için, rotate yapılandan parça alınıp asıl resme eklenecek;
image[225:225 + window_dimension_2[1], 525:525 + window_dimension_2[0]] = image_rotated_2[225:225 + window_dimension_2[1], 525:525 + window_dimension_2[0]]
cv2.imshow('Image with 2 Example', image)
cv2.waitKey(0)


# Save
cv2.imwrite("new_building.jpeg", image)