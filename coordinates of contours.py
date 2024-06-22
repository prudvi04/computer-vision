import cv2
import numpy as np

def find_contour_coordinates(image_path):
    # Step 1: Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Step 2: Find contours
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Step 3: Print coordinates of each contour
    for contour in contours:
        # Calculate the coordinates of the contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx, cy = 0, 0
        print(f"Contour centroid coordinates: ({cx}, {cy})")
        
        # Draw the contour on the original image
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        cv2.circle(image, (cx, cy), 7, (255, 0, 0), -1)  # Draw centroid
        
    # Step 4: Display the image with contours
    cv2.imshow("Contours", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
find_contour_coordinates('c:/th.jpeg')
