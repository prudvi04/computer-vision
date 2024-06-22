import cv2
import matplotlib.pyplot as plt

# Step 1: Read the Image
image_path = 'c:/th.jpeg'  # Path to the image file
original_image = cv2.imread(image_path)

# Convert BGR to RGB for displaying with matplotlib
original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

# Step 2: Resize the Image
# Define the new dimensions
larger_dimensions = (original_image.shape[1] * 2, original_image.shape[0] * 2)  # Double the size
smaller_dimensions = (original_image.shape[1] // 2, original_image.shape[0] // 2)  # Half the size

# Resize the images
larger_image = cv2.resize(original_image, larger_dimensions, interpolation=cv2.INTER_LINEAR)
smaller_image = cv2.resize(original_image, smaller_dimensions, interpolation=cv2.INTER_LINEAR)

# Convert resized images to RGB for displaying with matplotlib
larger_image_rgb = cv2.cvtColor(larger_image, cv2.COLOR_BGR2RGB)
smaller_image_rgb = cv2.cvtColor(smaller_image, cv2.COLOR_BGR2RGB)

# Step 3: Display All Images
plt.figure(figsize=(18, 6))

# Display Original Image
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(original_image_rgb)
plt.axis('off')

# Display Larger Image
plt.subplot(1, 3, 2)
plt.title('Larger Image')
plt.imshow(larger_image_rgb)
plt.axis('off')

# Display Smaller Image
plt.subplot(1, 3, 3)
plt.title('Smaller Image')
plt.imshow(smaller_image_rgb)
plt.axis('off')

plt.show()
