import pyvista as pv
import numpy as np
import vtk as _vtk
class Clipping:
    def __init__(self, controller, plotter,mesh_object):
        self.controller = controller
        self.plotter = plotter
        self.mesh_object=mesh_object

    def rectangle_picking_callback(self, cell_selection):
        self.plotter.clear()
        self.clipped_mesh = self.mesh_object.copy()
        self.clipped_mesh.add_point_data(cell_selection.points)
        if self.mesh_object.rgb_status==True:
            selected_indices = cell_selection["orig_id"]
            selected_color_data=self.controller.selected_mesh.color_data[selected_indices]
            self.clipped_mesh.add_color_data(selected_color_data)

        else:
            self.clipped_mesh.set_color_elevation()
        

        self.clipped_mesh.file_name = "Clipped " + self.clipped_mesh.file_name
        self.controller.add_db_tree_and_plotter(self.clipped_mesh)


        
 
#     # def disable(self):
#     #     for actor in self.text_actors:
#     #         self.plotter.remove_actor(actor)
#     #     for actor in self.point_actors:
#     #         self.plotter.remove_actor(actor)
#     #     self.plotter.remove_actor(self.line_actor)
#     #     self.plotter.disable_picking()