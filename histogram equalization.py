import cv2
import matplotlib.pyplot as plt

# Step 1: Read the Image
image_path = 'c:/th.jpeg'  # Path to the image file
original_image = cv2.imread(image_path)

# Step 2: Convert to Grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Histogram Equalization
equalized_image = cv2.equalizeHist(gray_image)

# Step 4: Display Both Images
plt.figure(figsize=(12, 6))

# Display Original Grayscale Image
plt.subplot(1, 2, 1)
plt.title('Original Grayscale Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

# Display Equalized Image
plt.subplot(1, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.show()
