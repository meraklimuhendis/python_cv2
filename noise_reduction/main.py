import cv2
import matplotlib.pyplot as plt
import numpy as np




image_file_path     = "image_noise.jpeg"
image               = cv2.imread(image_file_path)

# # Orginal
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.title("Building - Orginal")
# plt.show()


# Orginal
cv2.imshow('Noise Image - Orginal', image)
cv2.waitKey(0)

# image_removed_noise = cv2.fastNlMeansDenoising(image, None, 15, 15, 15) # Tek bir gri tonlamalı görüntüler için gürültü temizleme.
# cv2.imshow('Removed Noise', image_removed_noise)
# cv2.waitKey(0)

image_removed_noise = cv2.fastNlMeansDenoisingColored(image, None, 8, 5, 5) # Renkli görüntüler için gürültü temizleme. # Giriş, Çıktı, 
# cv2.fastNlMeansDenoising(src[, dst[, h[, templateWindowSize[, searchWindowSize ] ] ] ] ) → dst 
cv2.imshow('Removed Noise 2', image_removed_noise)
cv2.waitKey(0)


# Save
cv2.imwrite("image_removed_noise.jpeg", image_removed_noise)