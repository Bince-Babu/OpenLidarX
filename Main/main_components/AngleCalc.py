import pyvista as pv
import numpy as np
import matplotlib as plt
import vtk
class AngleCalc:
    def __init__(self,plotter):
        self.plotter = plotter
        self.selected_points = []
        self.line_actor=[]
        self.text_actors = []
        self.point_actors =[]
        self.labels = ['A', 'B', 'C']
        self.mesh_actor=None
        self.angle_display_actor=None

    def point_picking(self,point):
                self.selected_points.append(point)
                if len(self.selected_points) > 3:
                    print("hi")
                    for actor in self.text_actors:
                         self.plotter.remove_actor(actor)
                    for actor in self.point_actors:
                         self.plotter.remove_actor(actor)
                    for actor in self.line_actor:
                         self.plotter.remove_actor(actor)
                    self.plotter.remove_actor(self.line_actor)
                    self.plotter.remove_actor(self.mesh_actor)
                    self.plotter.remove_actor(self.angle_display_actor)
                    self.line_actor=[]
                    self.text_actors = []
                    self.point_actors =[]
                    self.mesh_actor=None
                    self.selected_points=self.selected_points[3:]
                    
                # print(selected_points)   
                self.point_actors.append(self.plotter.add_mesh(pv.PolyData(point), color='red',point_size=10, style='points',reset_camera=False,render_points_as_spheres=True))
                self.text_actors.append(self.plotter.add_point_labels(point,[f"{self.labels[len(self.selected_points)-1]}:\n X:{point[0]:.2f}\n Y:{point[1]:.2f}\n Z:{point[2]:.2f}"],font_size=24,show_points=False,shape_color="black",shape_opacity=0.6,always_visible=True,text_color="#CCCCCC"))

                                            
                
                if len(self.selected_points) == 2:
                    
                     self.line_actor.append(self.plotter.add_lines(np.array(self.selected_points[-2:]), color='red'))
                if len(self.selected_points) == 3:
                    self.line_actor.append(self.plotter.add_lines(np.array(self.selected_points[-2:]), color='red'))
                    arr=[]
                    arr.append(self.selected_points[0])
                    arr.append(self.selected_points[2])
                    self.line_actor.append(self.plotter.add_lines(np.array(arr), color='red'))
                    
                    v1 = np.array(self.selected_points[1]) - np.array(self.selected_points[0])
                    v2 = np.array(self.selected_points[2]) - np.array(self.selected_points[1])
                    v3 = np.array(self.selected_points[0]) - np.array(self.selected_points[2])
                    dot_product = np.dot(v1, v2)
                    magnitude_v1 = np.linalg.norm(v1)
                    magnitude_v2 = np.linalg.norm(v2)
                    magnitude_v3 = np.linalg.norm(v3)
                    angle_rad_A = np.arccos((magnitude_v1**2 + magnitude_v3**2 - magnitude_v2**2) / (2 * magnitude_v1 * magnitude_v3))
                    angle_rad_B = np.arccos((magnitude_v1**2 + magnitude_v2**2 - magnitude_v3**2) / (2 * magnitude_v1 * magnitude_v2))
                    angle_rad_C = np.arccos((magnitude_v2**2 + magnitude_v3**2 - magnitude_v1**2) / (2 * magnitude_v2 * magnitude_v3))
                    angle_deg_A = np.degrees(angle_rad_A)
                    angle_deg_B = np.degrees(angle_rad_B)
                    angle_deg_C = np.degrees(angle_rad_C)
                    # print(f"The angle at A is: {angle_deg_A:.2f} degrees")
                    # print(f"The angle at B is: {angle_deg_B:.2f} degrees")
                    # print(f"The angle at C is: {angle_deg_C:.2f} degrees")
                    s = (magnitude_v1 + magnitude_v2 + magnitude_v3) / 2
                    area = np.sqrt(s * (s - magnitude_v1) * (s - magnitude_v2) * (s - magnitude_v3))
                    # print(f"The area of the triangle is: {area:.2f} square units")
                    triangle_mesh = pv.PolyData(np.array(self.selected_points))
                    triangle_mesh.faces = [3, 0, 1, 2]  # Define the face of the triangle
                    self.mesh_actor=self.plotter.add_mesh(triangle_mesh, color='yellow', opacity=0.5)
                    info = f"""\
                    Angles:
                    A: {angle_deg_A:.2f} degrees
                    B: {angle_deg_B:.2f} degrees
                    C: {angle_deg_C:.2f} degrees

                    Area: {area:.2f} square units
                    """

                    # Add the text to the plotter
                    self.angle_display_actor=self.plotter.add_text(info, position='lower_left', font_size=10)
                    self.plotter.update()
    
    def disable(self):
            for actor in self.text_actors:
                self.plotter.remove_actor(actor)
            for actor in self.point_actors:
                self.plotter.remove_actor(actor)
            for actor in self.line_actor:
                self.plotter.remove_actor(actor)
            self.plotter.remove_actor(self.line_actor)
            self.plotter.remove_actor(self.mesh_actor)
            self.plotter.remove_actor(self.angle_display_actor)
            self.plotter.disable_picking()