import cv2
import numpy as np

# Load image
img_original = cv2.imread('Exp 4.jpg')

# Check if image loaded successfully
if img_original is None:
    print("Error: Image not found or path is incorrect.")
else:
    # Make a copy for marking corners
    img = img_original.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect corners using Shi-Tomasi method
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10)

    # Convert to integer values
    corners = corners.astype(int)

    # Draw small circles at each corner
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(img, (x, y), 4, (0, 255, 0), -1)

    # Display images
    cv2.imshow('Original Image', img_original)
    cv2.imshow('Shi-Tomasi Corners Detected', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
