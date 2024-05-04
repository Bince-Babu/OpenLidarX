import numpy as np
import pyvista as pv
import os
import copy
from PyQt5.QtCore import QObject
import pyvista as pv

class Mesh(QObject):
    def __init__(self):
        super().__init__()
       
        self.point_data = None
        self.color_data = None
        self.folder_name = None
        self.file_name = None
        self.polydata = None
        self.actor = None
        self.segment_id=None
        self.rgb_status = False
        self.cmap = None
    def add_point_data(self, point_data, update=False):
        self.point_data = point_data
        if update:
            self.polydata.points = point_data
            self.polydata["orig_id"] = np.arange(self.polydata.n_points)
        else:
            self.polydata = pv.PolyData(self.point_data)
            self.polydata["orig_id"] = np.arange(self.polydata.n_points)
        # if not update:
        #     self.polydata = pv.PolyData(self.point_data)
        # else:
        #     self.polydata.points = point_data

    def add_color_data(self, color_data):
        self.color_data = color_data
        self.polydata["color_by"] = self.color_data     
    def set_color_data(self):
        self.polydata["color_by"] = self.color_data
        self.rgb_status = True
    def set_color_elevation(self):
        self.polydata["color_by"] = self.point_data[:,2]
        self.rgb_status = False
    def add_file_name(self, file_name):
        self.folder_name, self.file_name = os.path.split(file_name)

    def copy(self):
        new_mesh = Mesh()
        new_mesh.rgb_status = copy.deepcopy(self.rgb_status)
        new_mesh.cmap = copy.deepcopy(self.cmap)
        new_mesh.point_data = copy.deepcopy(self.point_data)
        new_mesh.color_data = copy.deepcopy(self.color_data)
        new_mesh.folder_name = copy.deepcopy(self.folder_name)
        new_mesh.file_name = copy.deepcopy(self.file_name)
        new_mesh.polydata = self.polydata.copy() if self.polydata else None
        print("CoOOOOpy created")
        return new_mesh















        # if point_cloud is None:
        #     self.cloud_points = np.random.rand(100, 3)
        # else:
        #     self.cloud_points = point_cloud
        # self.poly_data = pv.PolyData(self.cloud_points)
        # if point_colors is not None:
        #     self.cloud_color = point_colors
        #     self.colors = self.colors - self.colors.min()
        #     self.poly_data.point_data["colors"] = self.colors
