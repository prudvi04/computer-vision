from PIL import Image
import matplotlib.pyplot as plt
image_path = 'C:/th.jpeg'
original_image = Image.open(image_path)
grayscale_image = original_image.convert('L')
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(original_image)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Grayscale Image')
plt.imshow(grayscale_image, cmap='gray')
plt.axis('off')
plt.show()
