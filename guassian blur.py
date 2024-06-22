import cv2
import matplotlib.pyplot as plt

# Step 1: Read the Image
image_path = 'c:/th.jpeg'  # Path to the image file
original_image = cv2.imread(image_path)

# Convert BGR to RGB for displaying with matplotlib
original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

# Step 2: Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(original_image, (15, 15), 0)

# Convert BGR to RGB for displaying with matplotlib
blurred_image_rgb = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)

# Step 3: Display Both Images
plt.figure(figsize=(12, 6))

# Display Original Image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(original_image_rgb)
plt.axis('off')

# Display Blurred Image
plt.subplot(1, 2, 2)
plt.title('Blurred Image')
plt.imshow(blurred_image_rgb)
plt.axis('off')

plt.show()
