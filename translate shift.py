import cv2
import numpy as np

def translate_image(image_path, tx, ty):
    # Step 2: Load the image
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load the image.")
        return
    
    # Get the dimensions of the image
    rows, cols = image.shape[:2]
    
    # Step 3: Define the translation matrix
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    
    # Step 4: Apply the translation
    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
    
    # Step 5: Display the original and translated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Translated Image', translated_image)

    # Wait for a key press and close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
translate_image('c:/th.jpeg', tx=100, ty=50)
