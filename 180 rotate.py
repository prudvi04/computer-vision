import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\th.jpeg')

# Get image dimensions
height, width = image.shape[:2]

# Define the transformation matrix for 180-degree rotation along the y-axis
matrix = np.array([[-1, 0, width - 1],
                   [0, 1, 0]], dtype=np.float32)

# Apply the transformation using warpAffine (not warpPerspective)
rotated_image = cv2.warpAffine(image, matrix, (width, height))

# Display the original and rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
