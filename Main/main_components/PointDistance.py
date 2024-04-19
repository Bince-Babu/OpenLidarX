import pyvista as pv
import numpy as np


class PointDistance:
    def __init__(self,plotter):
        self.plotter = plotter
        self.text_actors = []
        self.point_actors = []
        self.line_actor = None
        self.picked_points = []


    def distance_plot(self,point):
        self.picked_points.append(point)
        if len(self.picked_points) > 2:
            for actor in self.text_actors:
                self.plotter.remove_actor(actor)
            for actor in self.point_actors:
                self.plotter.remove_actor(actor)
            self.plotter.remove_actor(self.line_actor)

            self.line_actor=None
            self.text_actors = []
            self.point_actors =[]
            self.picked_points=self.picked_points[2:]
    
        
        self.point_actors.append(self.plotter.add_mesh(pv.PolyData(point), color='red', 
                                                 point_size=10, style='points',reset_camera=False,
                                                 render_points_as_spheres=True))
        self.text_actors.append(self.plotter.add_point_labels(point,[f"Picked Point:\n X:{point[0]:.2f}\n Y:{point[1]:.2f}\n Z:{point[2]:.2f}"],
                                                                font_size=24,show_points=False,
                                                                shape_color="black",shape_opacity=0.6,
                                                                always_visible=True,text_color="#CCCCCC"))
        
        if len(self.picked_points)==2:
            self.line_actor = self.plotter.add_lines(np.array(self.picked_points), color='red')
            text,mid_point = self.calculate_distance()
            self.text_actors.append(self.plotter.add_point_labels(mid_point,text,
                                                                font_size=24,show_points=False,
                                                                shape_color="red",shape_opacity=0.9,
                                                                always_visible=True,text_color="#CCCCCC"))
        if len(self.picked_points)>2:
            pass        

    def calculate_distance(self):
        x_1, y_1,z_1 = self.picked_points[0]
        x_2, y_2,z_2 = self.picked_points[1]
        euclid_distance = ((x_1-x_2)**2 + (y_1 - y_2)**2 + (z_1 - z_2)**2)**0.5
        mid_point_x = (x_1+x_2)/2  
        mid_point_y = (y_1+y_2)/2
        mid_point_z = (z_1+z_2)/2
        return [f"Distance: \n {euclid_distance:.5f} m"], [mid_point_x,mid_point_y,mid_point_z]
    
    def disable(self):
        for actor in self.text_actors:
            self.plotter.remove_actor(actor)
        for actor in self.point_actors:
            self.plotter.remove_actor(actor)
        self.plotter.remove_actor(self.line_actor)
        self.plotter.disable_picking()