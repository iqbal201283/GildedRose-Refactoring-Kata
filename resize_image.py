import cv2

image = cv2.imread("/home/bpd/Desktop/EPM/eastern-province-municipality-logo.png")

image = cv2.resize(image, (125, 125))

cv2.imwrite("/home/bpd/Desktop/EPM/eastern-province-municipality-logo_2.png", image)
