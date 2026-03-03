from core.depth import load_depth
from core.loader import load_image
from core.pointcloud import point_cloud
from core.viewer import view_pointcloud
from utils.normalize import normalize_image
from utils.visualization import compare_image
from config import full_path
from pathlib import Path
import sys  

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = Path(sys.argv[1])
    else:
        image_path = full_path

    image = load_image(full_path)
    depth_map = load_depth(image)
    normalized_depth = normalize_image(depth_map)
    compare_image(image, normalized_depth)
    points, colors = point_cloud(image, depth_map)
    view_pointcloud(points, colors)
