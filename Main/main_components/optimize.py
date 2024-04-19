import pyvista as pv
import numpy as np
def optimized(cloud):
    reduction_ratio = 0.5
    old_points_num = cloud.number_of_points
    new_points_num = int(old_points_num * reduction_ratio)
    
    downsampled_indices = np.random.choice(old_points_num , new_points_num, replace=False)
    new_cloud_points = cloud.points[downsampled_indices]
    new_cloud = pv.PolyData(new_cloud_points)

    return new_cloud