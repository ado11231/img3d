# Takes 3D points and RGB colors and renders an interactive Open3D point cloud viewer.
# Colors are divided by 255 because Open3D expects values between 0 and 1.

import open3d

def view_pointcloud(points, colors):
    pcd = open3d.geometry.PointCloud()
    pcd.points = open3d.utility.Vector3dVector(points)
    pcd.colors = open3d.utility.Vector3dVector(colors /255.0)
    open3d.visualization.draw_geometries([pcd])

