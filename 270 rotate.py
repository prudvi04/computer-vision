import cv2

# Step 2: Load the image
image = cv2.imread('c:/th.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Step 3a: Rotate the image 90 degrees counterclockwise
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    # Step 3b: Flip the rotated image horizontally (equivalent to 270-degree rotation along the y-axis)
    rotated_flipped_image = cv2.flip(rotated_image, 1)

    # Step 4: Display the original and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('270 Degree Rotated Image', rotated_flipped_image)

    # Wait for a key press and close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
