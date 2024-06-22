import cv2

# Function to display coordinates on left mouse click
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates: ({x}, {y})")

# Read an image
image_path = 'c:/th.jpeg'  # Replace with your image path
image = cv2.imread(image_path)

# Check if image is loaded correctly
if image is None:
    print(f"Error: Unable to load image at {image_path}")
else:
    # Display the image
    cv2.imshow('Image', image)

    # Set mouse callback function
    cv2.setMouseCallback('Image', click_event)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
