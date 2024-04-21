from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def apply_sepia(image):
    """
    Applies a sepia filter to an image using dot product.

    Args:
        image: A PIL Image object.

    Returns:
        A PIL Image object with the sepia filter applied.
    """

    image_array = np.array(image)

    # Check if the image is grayscale (has only one channel)
    if len(image_array.shape) == 2:
        height, width = image_array.shape
        image_array = np.stack((image_array,)*3, axis=-1)
    else:
        height, width, _ = image_array.shape

    # Sepia tone coefficients
    sepia_matrix = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])

    # Reshape image into a 2D array of pixels (flattening each channel)
    image_array_reshaped = image_array.reshape(-1, 3)

    # Apply sepia transformation using dot product
    sepia_image = image_array_reshaped.dot(sepia_matrix)

    # Reshape back to image format and clip values
    sepia_image = sepia_image.reshape(height, width, 3)
    sepia_image = np.clip(sepia_image, 0, 255).astype(np.uint8)

    return Image.fromarray(sepia_image)

def visualize_sepia(original_image, sepia_image):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original_image)
    axes[0].set_title("Original Image")
    axes[1].imshow(sepia_image)
    axes[1].set_title("Sepia Filtered Image")
    plt.show()

# Usage:
original_image = Image.open(r"c:\users\nicol\desktop\cs.jpg")
sepia_image = apply_sepia(original_image)
visualize_sepia(original_image, sepia_image)