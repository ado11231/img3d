# Takes the original image and depth map and converts every pixel into a 3D point.
# Back-projection formula: X = (u - cx) * depth / fx, Y = (v - cy) * depth / fy, Z = depth
# Returns points (N, 3) with XYZ coordinates and colors (N, 3) with RGB values.

import numpy as np
from config import FX, FY, CX, CY

def point_cloud(image, depth_image):
    height, width = image.shape[:2]

    u, v = np.meshgrid(np.arange(width), np.arange(height))

    x = (u - CX) * depth_image / FX
    y = (v - CY) * depth_image / FY
    z = depth_image

    x = x.flatten()
    y = y.flatten()
    z = z.flatten()

    points = np.column_stack((x,y,z))

    colors = image.reshape(-1, 3)

    return points, colors