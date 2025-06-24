import cv2
import numpy as np

# Load the image
image = cv2.imread('/home/bpd/Downloads/car_number_plate.png')

# Resize image by a factor of 2 using nearest-neighbor interpolation
resized_image = cv2.resize(image, None, fx=15, fy=15, interpolation=cv2.INTER_NEAREST)

kernel = np.ones((31, 31), np.uint8)
eroded = cv2.erode(resized_image, kernel, iterations=1)

dilated = cv2.dilate(eroded, kernel, iterations=1)

# Save the output
cv2.imwrite('output.jpg', resized_image)
