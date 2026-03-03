import numpy as np
from numpy.typing import NDArray

# MiDaS outputs raw float32 depth values in an unpredictable range.
# We normalize to 0-255 so it can be displayed as an image.
# Formula: (value - min) / (max - min) * 255
# Then convert to uint8 since pixels must be whole numbers between 0-255.
def normalize_image(image: NDArray[np.float32]) -> NDArray[np.uint8]:
    min_val = image.min()
    max_val = image.max()

    fixed = (image - min_val) / (max_val - min_val) * 255

    fixed = fixed.astype(np.uint8)

    return fixed










