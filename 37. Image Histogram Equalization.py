import cv2

img = cv2.imread('Exp 4.jpg', 0)
equalized = cv2.equalizeHist(img)

cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
