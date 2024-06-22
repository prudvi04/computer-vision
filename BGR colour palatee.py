import cv2
import numpy as np

def bgr_color_palette():
    # Callback function for trackbar changes (does nothing)
    def nothing(x):
        pass

    # Create a black image window
    img = np.zeros((200, 600, 3), np.uint8)
    cv2.namedWindow('BGR Color Palette')

    # Create trackbars for color change
    cv2.createTrackbar('Blue', 'BGR Color Palette', 0, 255, nothing)
    cv2.createTrackbar('Green', 'BGR Color Palette', 0, 255, nothing)
    cv2.createTrackbar('Red', 'BGR Color Palette', 0, 255, nothing)

    while True:
        # Get current positions of trackbars
        blue = cv2.getTrackbarPos('Blue', 'BGR Color Palette')
        green = cv2.getTrackbarPos('Green', 'BGR Color Palette')
        red = cv2.getTrackbarPos('Red', 'BGR Color Palette')

        # Update the image with the current BGR values
        img[:] = [blue, green, red]

        # Display the image
        cv2.imshow('BGR Color Palette', img)

        # Exit loop when 'Esc' key is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

# Example usage
bgr_color_palette()
