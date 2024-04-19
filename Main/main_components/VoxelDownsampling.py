import pyvista as pv
import numpy as np
import os
class VoxelDownsampling:
    def __init__(self,controller):
        self.controller = controller
        self.selected_mesh = self.controller.selected_mesh
        self.mesh_points = self.selected_mesh.point_data
        self.mesh_colors = self.selected_mesh.color_data
        print(self.controller.message)
        self.controller.view.plotter_widget.plotter.add_slider_widget(lambda slider_value: self.decimate_cloud(slider_value),[1,100], title="Reduction Ratio", value=100, color="white")
        
    def decimate_cloud(self,slider_value):
        # # print("Slider value:", slider_value)
        # self.cloud = pv.read("cloud.vtk")
        slider_value = round(slider_value,2)
        reduction_ratio = slider_value/100
        old_points_num = self.mesh_points.shape[0]
        new_points_num = int(old_points_num * reduction_ratio)
        downsampled_indices = np.random.choice(old_points_num , new_points_num, replace=False)
        self.new_polydata = pv.PolyData(np.asarray(self.mesh_points[downsampled_indices]))
        self.new_polydata["color_by"] = np.asarray(self.mesh_colors[downsampled_indices])
        # camera_position = self.controller.view.plotter_widget.plotter.camera.position
        self.controller.view.plotter_widget.plotter.remove_actor(self.selected_mesh.actor)
        self.selected_mesh.actor = self.controller.view.plotter_widget.plotter.add_mesh(self.new_polydata,scalars='color_by',rgb = self.selected_mesh.rgb_status,point_size = 0.5,reset_camera = False)
        # self.controller.view.plotter_widget.plotter.camera.position = camera_position
    def disable(self):
        self.selected_mesh.polydata = self.new_polydata
        self.selected_mesh.polydata = self.new_polydata
        self.controller.view.plotter_widget.plotter.clear_slider_widgets()


        
