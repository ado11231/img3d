# Loads an image from disk using OpenCV and converts BGR to RGB.
# Raises a clear error if the file is not found rather than passing None downstream.
# Returns a NumPy array shaped (height, width, 3).

import cv2 as cv

def load_image(path):
    img = cv.imread(str(path))
    if img is None:
        raise FileNotFoundError("Could Not Find Image")
    
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    return img_rgb