import cv2
import numpy as np

def modify_roi(image_path, top_left, bottom_right, color=(0, 255, 0)):
    # Step 2: Load the image
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load the image.")
        return
    
    # Step 3: Define the ROI
    x1, y1 = top_left
    x2, y2 = bottom_right

    # Ensure coordinates are within image bounds
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(image.shape[1], x2), min(image.shape[0], y2)
    
    # Step 4: Modify the ROI
    image[y1:y2, x1:x2] = color  # Fill the ROI with the specified color
    
    # Step 5: Display the original and modified images
    cv2.imshow('Modified Image', image)

    # Wait for a key press and close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
modify_roi('c:/th.jpeg', top_left=(50, 50), bottom_right=(200, 200), color=(255, 0, 0))
