import cv2
import matplotlib.pyplot as plt

def plot_color_histogram(image_path):
    # Step 1: Read the Image
    image = cv2.imread(image_path)
    
    # Convert BGR to RGB for displaying with matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Step 2: Calculate Histograms
    # Split the image into its color channels
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')
    channel_names = ('Blue', 'Green', 'Red')
    
    plt.figure(figsize=(18, 6))
    
    # Plot the original image
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image_rgb)
    plt.axis('off')
    
    # Plot the histograms
    plt.subplot(1, 2, 2)
    plt.title('Color Histograms')
    
    for channel, color, name in zip(channels, colors, channel_names):
        histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=name)
        plt.xlim([0, 256])
    
    plt.legend()
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.show()

# Example usage
image_path = 'c:/th.jpeg'  # Replace with the path to your image file
plot_color_histogram(image_path)
