import cv2
import matplotlib.pyplot as plt

# Function to perform a 90-degree clockwise rotation
def rotate_image_90_clockwise(image_path):
    # Step 1: Read the Image
    image = cv2.imread(image_path)
    
    # Convert BGR to RGB for displaying with matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Step 2: Rotate the Image 90 degrees clockwise
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    
    # Convert BGR to RGB for displaying with matplotlib
    rotated_image_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
    
    # Step 3: Display Both Images
    plt.figure(figsize=(12, 6))
    
    # Display Original Image
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image_rgb)
    plt.axis('off')
    
    # Display Rotated Image
    plt.subplot(1, 2, 2)
    plt.title('90-degree Clockwise Rotated Image')
    plt.imshow(rotated_image_rgb)
    plt.axis('off')
    
    plt.show()

# Example usage
image_path = 'c:/th.jpeg'  # Replace with the path to your image file
rotate_image_90_clockwise(image_path)
