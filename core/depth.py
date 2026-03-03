import torch
import cv2 as cv
from config import MIDAS_SMALL, device

# Loads MiDaS model and transform from torch.hub.
# Preprocesses the image into the format MiDaS expects.
# Runs inference to produce raw depth values.
# Resizes depth output to match original image dimensions.
# Returns depth map as a float32 NumPy array.
def load_depth(image):
    model_type = MIDAS_SMALL
    midas = torch.hub.load("intel-isl/MiDaS", model_type)
    midas.to(device)
    midas.eval()    

    midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

    if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
        transform = midas_transforms.dpt_transform
    else:
        transform = midas_transforms.small_transform

    input_batch = transform(image).to(device)

    with torch.no_grad():
        prediction = midas(input_batch)

        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size = image.shape[:2],
            mode = "bicubic",
            align_corners = False,
        ).squeeze()

    output = prediction.cpu().numpy()

    return output


