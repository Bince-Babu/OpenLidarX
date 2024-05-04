import pyvista as pv
import vtk as _vtk
class PointPicker:
    def __init__(self,plotter):
        self.plotter = plotter
        self.text_actor = None
        self.point_actor = None
    def point_picking(self,points):
        self.point_actor = self.plotter.add_mesh(pv.PolyData(points), color='red', 
                                                 point_size=5, style='points',reset_camera=False,
                                                 render_points_as_spheres=True,name='point')
        self.text_actor = self.plotter.add_point_labels(points,[f"Picked Point:\n X:{points[0]:.2f}\n Y:{points[1]:.2f}\n Z:{points[2]:.2f}"],
                                                                font_size=24,show_points=False,
                                                                shape_color="black",shape_opacity=0.8,
                                                                always_visible=True,text_color="#CCCCCC",name='point_label')
    def disable(self):
        try:
            self.plotter.remove_actor(self.plotter.actors['point'])
            self.plotter.remove_actor(self.plotter.actors['point_label-labels'])
            
            self.plotter.clear_box_widgets()
        except:
            print("No actor to remove")
        finally:
            self.plotter.disable_picking()