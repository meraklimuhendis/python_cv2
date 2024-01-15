import cv2
import matplotlib.pyplot as plt




image_file_path = "forest.jpeg"
image           = cv2.imread(image_file_path)       # Dosya cv2 ile okunacak.
image_gray      = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Image Orginal
cv2.imshow('Forest - Orginal', image)
cv2.waitKey(0)

# Image Gray Tone
cv2.imshow('Forest - Gray Tone', image_gray)
cv2.waitKey(0)

# Save
cv2.imwrite("forest_gray.jpeg", image_gray)


## Rectangle
y, x, z = image.shape
print("image_gray", x, y, z)    # image_gray 1600 1066 3
rectangle_color     = (0, 0, 0) # black
rectangle_dimension = 100        # px

point_1  = [(0, 0), (rectangle_dimension, rectangle_dimension)] # Point 1, index start-end, Left top
point_2  = [(0, y - rectangle_dimension), (rectangle_dimension, y)] # Point 2, index start-end, Left bottom
point_3  = [(x - rectangle_dimension, 0), (x, rectangle_dimension)] # Point 3, index start-end, Right top
point_4  = [(x - rectangle_dimension, y - rectangle_dimension), (x, y)] # Point 4, index start-end, Right bottom

cv2.rectangle(image_gray, point_1[0], point_1[1], rectangle_color, -1) # Left top
cv2.rectangle(image_gray, point_2[0], point_2[1], rectangle_color, -1) # Left bottom
cv2.rectangle(image_gray, point_3[0], point_3[1], rectangle_color, -1) # Right top
cv2.rectangle(image_gray, point_4[0], point_4[1], rectangle_color, -1) # Right bottom

# Image Gray Tone With Rectangle
cv2.imshow('Forest - Gray Tone With Rectangle', image_gray)
cv2.waitKey(0)

# Save
cv2.imwrite("forest_gray_with_rectangle.jpeg", image_gray)