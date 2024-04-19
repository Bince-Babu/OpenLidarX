import os
import CSF
import numpy as np
from PyQt5.QtCore import QThread
from typing import List, Tuple
import copy
import laspy
import pickle
from PyQt5.QtWidgets import QMenuBar, QAction, QFileDialog
import pyvista as pv # only for testing
class Ground_filtering(QThread):
    def __init__(self,controller,mesh_object):
        super().__init__()
        self.controller = controller
        print("LLLLLLLLLLLLLLLL")
        self.mesh_object = mesh_object
        self.start()

    def run(self):
        xyz = self.mesh_object.polydata.points
        xyz = xyz/1000
        print("XYZ"," ",xyz)
        csf = CSF.CSF()
        csf.params.bSloopSmooth = False
        csf.params.cloth_resolution = 0.5
        csf.setPointCloud(xyz)
        ground = CSF.VecInt()  # a list to indicate the index of ground points after calculation
        non_ground = CSF.VecInt() # a list to indicate the index of non-ground points after calculation
        csf.do_filtering(ground, non_ground) # do actual filtering
        print(np.array(ground))
        self.ground_mesh = self.mesh_object.copy()
        self.ground_mesh.add_point_data((xyz[np.array(ground)])*1000)
        self.ground_mesh.add_color_data(self.mesh_object.color_data[np.array(ground)])
        self.ground_mesh.file_name = "Ground " + self.ground_mesh.file_name
        self.non_ground_mesh = self.mesh_object.copy()
        self.non_ground_mesh.add_point_data((xyz[np.array(non_ground)])*1000)
        self.non_ground_mesh.add_color_data(self.mesh_object.color_data[np.array(non_ground)])
        self.non_ground_mesh.file_name = "Non-Ground " + self.non_ground_mesh.file_name
        self.controller.view.signals.remove_mesh_signal.emit(self.mesh_object)
        print("MESH REMOVED")
        self.controller.add_db_tree_and_plotter(self.ground_mesh)
        self.controller.add_db_tree_and_plotter(self.non_ground_mesh)
        print("Ground_filtering completed")
class Worker(QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        k = 0
        for i in range(10):
            print(i)
