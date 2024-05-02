from DataModel import DataModel
import pyvista as pv
import numpy as np
import os
from segment_lidar import samlidar
class InstanceSegmentation:
    def __init__(self, controller, plotter,mesh_object):
        self.controller = controller
        self.plotter = plotter
        self.mesh_object=mesh_object

    def segment(self):
        self.copymesh = self.mesh_object.copy()
        actual_file_path = os.path.join(self.copymesh.folder_name, self.copymesh.file_name)
        model = samlidar.SamLidar(ckpt_path="sam_vit_h_4b8939.pth")
        points = model.read(actual_file_path)
        
        cloud, non_ground, ground = model.csf(points)
        labels, *_ = model.segment(points=cloud, image_path="raster.tif", labels_path="labeled.tif")
        model.write(points=points, non_ground=non_ground, ground=ground, segment_ids=labels, save_path="segmented.las")
        print("Segmentation completed")
        model_creator = DataModel()
        
        mesh_objects = model_creator.file_process("segmented.las")
        self
        mesh_objects.file_name = "Segmented " + self.copymesh.file_name
        self.controller.add_db_tree_and_plotter(mesh_objects)




        
        
 
#     # def disable(self):
#     #     for actor in self.text_actors:
#     #         self.plotter.remove_actor(actor)
#     #     for actor in self.point_actors:
#     #         self.plotter.remove_actor(actor)
#     #     self.plotter.remove_actor(self.line_actor)
#     #     self.plotter.disable_picking()