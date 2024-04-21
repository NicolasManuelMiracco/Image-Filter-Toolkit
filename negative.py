from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def apply_negative(image):
    """
    Applies a negative filter to an image.

    Args:
        image: A PIL Image object.

    Returns:
        A PIL Image object with the negative filter applied.
    """

    image_array = np.array(image)
    # Invert image colors
    negative_image = 255 - image_array
    # Clip values to ensure they are within [0, 255] range and avoid data type overflow
    negative_image = np.clip(negative_image, 0, 255).astype(np.uint8)

    return Image.fromarray(negative_image)

def visualize_comparison(original_image, processed_image):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original_image)
    axes[0].set_title("Original Image")
    axes[1].imshow(processed_image)
    axes[1].set_title("Processed Image")
    plt.show()

# Usage:
original_image = Image.open(r"c:\users\nicol\desktop\cs.jpg")
negative_image = apply_negative(original_image)
visualize_comparison(original_image, negative_image)
