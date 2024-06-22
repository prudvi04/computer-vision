import cv2
import numpy as np

def apply_averaging_filter(image_path, kernel_size=(5, 5)):
    # Step 2: Load the image
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load the image.")
        return
    
    # Step 3: Apply the averaging filter using OpenCV's blur function
    smoothed_image = cv2.blur(image, kernel_size)
    
    # Alternatively, we can create the kernel manually and use filter2D
    # kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])
    # smoothed_image = cv2.filter2D(image, -1, kernel)
    
    # Step 4: Display the original and smoothed images
    cv2.imshow('Original Image', image)
    cv2.imshow('Smoothed Image', smoothed_image)

    # Wait for a key press and close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
apply_averaging_filter('c:/th.jpeg', kernel_size=(5, 5))
