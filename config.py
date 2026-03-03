from pathlib import Path
import torch

path = Path('assets/images')
image = 'image.jpg'
full_path = path / image

MIDAS_SMALL = "MiDaS_small"
device = 'cuda' if torch.cuda.is_available() else 'cpu'

IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480
FX = IMAGE_WIDTH
FY = IMAGE_WIDTH
CX = IMAGE_WIDTH / 2
CY = IMAGE_HEIGHT / 2
