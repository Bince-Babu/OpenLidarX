from main_components.InstanceSegmentation import InstanceSegmentation
from main_components.Clipping import Clipping
from main_components.AngleCalc import AngleCalc
from PyQt5.QtWidgets import QFileDialog
import numpy as np
from main_components.Signals import Signals
import files_handler
import time
from main_components.ICPRegistration import ICPRegistration
from main_components.PointPicker import PointPicker
from main_components.PointDistance import PointDistance
from main_components.VoxelDownsampling import VoxelDownsampling
from main_components.View_updater import View_updater
import pyvista as pv
import os
from main_components.ground_filtering import Ground_filtering
class DataFlowController:
    def __init__(self,model,view):
        """
        param:
        """
        self.model = model
        self.message = "Hello from Controller"
        self.view = view
        self.view.signals.file_dialog_triggered.connect(self.handle_file_open)
        self.view.signals.add_mesh_signal.connect(self.show_mesh)
        self.view.signals.update_mesh_signal.connect(self.update_mesh)
        self.view.signals.remove_mesh_signal.connect(self.remove_mesh)
        self.view.signals.registration_triggered.connect(self.handle_registration)
        self.view.signals.point_picking_signal_enable.connect(self.point_picking_enable)
        self.view.signals.point_picking_signal_disable.connect(self.point_picking_disable)
        self.view.signals.distance_measure_enable.connect(self.distance_measure_enable)
        self.view.signals.distance_measure_disable.connect(self.distance_measure_disable)
        self.view.signals.view_change_signal.connect(self.view_handler)
        self.view.signals.dbtree_select_signal.connect(self.dbtree_select)
        self.view.signals.downsample_enable.connect(self.downsample_enable)
        self.view.signals.downsample_disable.connect(self.downsample_disable)
        self.view.signals.ground_filtering_signal.connect(self.ground_filtering)
        self.view.signals.angle_calc_enable.connect(self.angle_calc_enable)
        self.view.signals.angle_calc_disable.connect(self.angle_calc_disable)
        self.view.signals.clipping_enable.connect(self.clipping_enable)
        self.view.signals.clipping_disable.connect(self.clipping_disable)
        self.view.signals.instance_segmentation_signal.connect(self.instance_segmentation)
        self.registration_object = None
        self.view_object = View_updater(self.view.plotter_widget.plotter)
        self.selected_mesh = None
    def update_mesh(self,mesh_object):
        print("Update mesh triggered")
    def ground_filtering(self):
        print("Ground filtering initiated")
        self.ground_filtering = Ground_filtering(self,self.selected_mesh)
        self.ground_filtering.start()
        #ground_filtering.wait()
        print("THread completed")
    def dbtree_select(self,mesh_object):
        print("Select signal working")
        self.selected_mesh = mesh_object
        self.view.left_widget.list_widget.update_list_widget(mesh_object)
    def view_handler(self,view):
        self.view_object.update_view(view)
    def handle_file_open(self):

        mesh_objects = self.handle_file_dialog()
        for mesh_object in mesh_objects:
            self.add_db_tree_and_plotter(mesh_object)
    def downsample_enable(self):
        #self.view.plotter_widget.plotter.clear()
        self.downsample = VoxelDownsampling(self)
        # self.view.plotter_widget.plotter.enable_point_picking(callback = self.point_picker.point_picking,show_point = False)
    def downsample_disable(self):

        try:
            
            self.downsample.disable()
        except:
            print("Voxel Downsampling is not enabled")
    def handle_registration(self):
        print("Registration function triggered")
        mesh_objects = self.handle_file_dialog()
        if self.registration_object == None:
            self.registration_object = ICPRegistration(self)
        self.registration_object.do_registration(mesh_objects)
        registered_mesh = self.registration_object.return_registered_mesh()
        if registered_mesh != None:
            self.add_db_tree_and_plotter(registered_mesh)
    def handle_file_dialog(self):
        

        
        return  files_handler.file_handle_window()
    def show_mesh(self,mesh_object):
        print("Show mesh triggered")
        # print("in show mesh" , " " ,mesh_object.polydata.points.shape)
        

        # print("in show mesh" , " " ,mesh_object.polydata["color_by"].shape)
        mesh_object.actor = self.view.plotter_widget.plotter_add_mesh(mesh_object,False)    #ADD MORE DETAILS  When the plotter clear attribute is given as true and is checked or unchecked a problem is there 
        print(mesh_object.polydata.points.shape)
    def add_db_tree_and_plotter(self,mesh_object):
        self.view.nav_bar.point_pick.setEnabled(True)
        self.view.nav_bar.distance.setEnabled(True)
        self.view.nav_bar.downsample.setEnabled(True)
        self.view.nav_bar.angle.setEnabled(True)
        self.view.left_widget.tree_widget.update_tree_widget(mesh_object)
        self.view.signals.add_mesh_signal.emit(mesh_object)       
    def remove_mesh(self,mesh_object):
        self.view.plotter_widget.plotter.remove_actor(mesh_object.actor)
    def point_picking_enable(self):
    
        print("Point Picking Initiaited")
        self.view.nav_bar.distance.setEnabled(False)
        self.point_picker = PointPicker(self.view.plotter_widget.plotter)
        self.view.plotter_widget.plotter.enable_point_picking(callback = self.point_picker.point_picking,show_point = False)
    def point_picking_disable(self):
        print("point picking disabled")
        self.view.nav_bar.distance.setEnabled(True)
        try:
            self.point_picker.disable()
        except:
            print("Point Picking is not enabled")
    def distance_measure_enable(self):
            

        self.point_distance = PointDistance(self.view.plotter_widget.plotter)
        self.view.nav_bar.point_pick.setEnabled(False)
        self.view.plotter_widget.plotter.enable_point_picking(callback = self.point_distance.distance_plot,show_point = False)
    def distance_measure_disable(self):

        self.view.nav_bar.point_pick.setEnabled(True)
        try:
            self.point_distance.disable()
        except:
            print("Distance Measurement is not enabled")
    
    def angle_calc_enable(self):
        print("Angle Enabled")
        self.anglecalc = AngleCalc(self.view.plotter_widget.plotter)
        self.view.plotter_widget.plotter.enable_point_picking(callback = self.anglecalc.point_picking,show_point=False)

    def angle_calc_disable(self):
        try:
            self.anglecalc.disable()
        except:
            print("Angle calculation is not enabled")
    def clipping_enable(self):
        print("Clipping Enabled")
        self.clip = Clipping(self, self.view.plotter_widget.plotter,self.selected_mesh)
        self.view.plotter_widget.plotter.enable_cell_picking(callback= self.clip.rectangle_picking_callback, show_message=True, font_size=18, start=True,style='points')

    def clipping_disable(self):
        try:
            self.clip.disable()
        except:
            print("Point Picking is not enabled")
    def instance_segmentation(self):
        self.instancesegmentation=InstanceSegmentation(self,self.view.plotter_widget.plotter,self.selected_mesh)
        self.instancesegmentation.segment()
       
        





























