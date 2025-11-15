import cv2

img = cv2.imread('Mocha.jpg')
blur = cv2.GaussianBlur(img, (25, 25), 5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Blurred Image', blur)
cv2.imshow('Gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()