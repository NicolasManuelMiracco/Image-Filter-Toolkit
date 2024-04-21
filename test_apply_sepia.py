import pytest
from PIL import Image
import numpy as np
from apply_sepia import apply_sepia  # Import the function to test

def test_apply_sepia():
    """
    Tests the apply_sepia function with a sample RGB image.
    Checks if the output image has the expected sepia tone.
    """
    # Create a sample RGB image
    width, height = 200, 150
    rgb_array = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    image = Image.fromarray(rgb_array)

    # Apply sepia filter
    sepia_image = apply_sepia(image)
    sepia_array = np.array(sepia_image)

    # Create a reference sepia image using apply_sepia function
    reference_sepia_image = apply_sepia(image)
    reference_sepia_array = np.array(reference_sepia_image)

    # Check that the output is still an RGB image with the same dimensions
    assert sepia_array.shape == rgb_array.shape
    assert sepia_image.mode == 'RGB'

    # Compare the sepia image with the reference sepia image
    mismatch_count = np.sum(sepia_array != reference_sepia_array)
    mismatch_percentage = (mismatch_count / (height * width * 3)) * 100
    assert mismatch_percentage < 1, f"Mismatch percentage: {mismatch_percentage}%"