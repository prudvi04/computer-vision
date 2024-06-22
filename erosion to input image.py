import cv2
import numpy as np

def apply_erosion(image_path, kernel_size=(5, 5), iterations=1):
    # Step 2: Load the image
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load the image.")
        return

    # Step 3: Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Step 4: Apply a binary threshold to the image
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    
    # Step 5: Define the kernel for erosion
    kernel = np.ones(kernel_size, np.uint8)
    
    # Apply erosion
    eroded_image = cv2.erode(binary_image, kernel, iterations=iterations)
    
    # Step 6: Display the original and eroded images
    cv2.imshow('Original Image', binary_image)
    cv2.imshow('Eroded Image', eroded_image)

    # Wait for a key press and close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
apply_erosion('c:/th.jpeg')
