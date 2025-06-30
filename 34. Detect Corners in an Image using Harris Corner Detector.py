import cv2
import numpy as np

# Load image
img_original = cv2.imread('Exp 3.jpg')

# Check if image loaded successfully
if img_original is None:
    print("Error: Image not found or path is incorrect.")
else:
    # Make a copy to work on
    img = img_original.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    # Result is dilated for marking corners
    dst = cv2.dilate(dst, None)

    # Threshold for optimal value and mark in red
    img[dst > 0.01 * dst.max()] = [0, 0, 255]

    # Display images
    cv2.imshow('Original Image', img_original)
    cv2.imshow('Harris Corners Detected', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
