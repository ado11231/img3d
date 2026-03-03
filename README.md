img3d

A computer vision pipeline that converts 2D images into interactive 3D point clouds using MiDaS depth estimation.

Steps:
1. Loads a 2D image
2. Runs MiDaS to estimate depth for every pixel
3. Displays the original image alongside its depth heatmap
4. Converts every pixel into a 3D point using back-projection
5. Renders an interactive 3D point cloud you can rotate around

Stack:
- OpenCV — image loading and color conversion
- PyTorch + MiDaS — AI depth estimation
- NumPy — array manipulation
- Matplotlib — depth map visualization
- Open3D — interactive 3D point cloud viewer

Setup: (bash)
python3.11 -m venv venv
source venv/bin/activate
pip install opencv-python numpy matplotlib open3d streamlit timm
pip install torch torchvision torchaudio


Usage:

Run with default image from config:
python3 main.py

Run with a custom image:
python3 main.py /path/to/your/image.jpg

Project Structure:

img3d/
├── main.py              # pipeline orchestrator
├── config.py            # settings and camera intrinsics
├── core/
│   ├── loader.py        # image loading
│   ├── depth.py         # MiDaS depth estimation
│   ├── pointcloud.py    # back-projection 2D to 3D
│   └── viewer.py        # Open3D visualization
├── utils/
│   ├── normalize.py     # depth map normalization
│   └── visualization.py # side by side display
└── assets/
    └── images/          # input images
```
