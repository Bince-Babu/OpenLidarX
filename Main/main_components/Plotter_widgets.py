from PyQt5.QtWidgets import QVBoxLayout,QWidget, QFrame
from pyvistaqt import QtInteractor
import pyvista as pv
class PlotterWidget(QWidget):
    def __init__(self):
        super().__init__()
        # self.plotter = QtInteractor(self)
        # self.plotter.set_background('red', top="#0a6595")
        # self.plotter.add_camera_orientation_widget()
        # self.plane = pv.Plane()
        # #self.plotter.add_mesh(self.plane)
        # layout = QVBoxLayout()
        # layout.addWidget(self.plotter)
        # self.setLayout(layout)
        # self.plotter.render_to_window = False
        self.plotter = QtInteractor(self)
        self.plotter.set_background('#12284a', top="#12284a")
        self.plotter.add_camera_orientation_widget()
        # Create a frame to embed the plotter
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("QFrame { background-color: #12284a; border-radius: 20px; }")  # Adjust border-radius as needed
        
        # Add the plotter to the frame
        layout = QVBoxLayout(frame)
        layout.addWidget(self.plotter)
        frame.setLayout(layout)
        # Set layout for the PlotterWidget
        layout = QVBoxLayout(self)
        layout.addWidget(frame)
        self.setLayout(layout)

    def clear_plotter(self):
        self.plotter.clear()
    def plotter_add_mesh(self,mesh_object,plotter_clear = True):
        if plotter_clear == True:
            self.clear_plotter()
            

            if mesh_object.cmap is  None:
                return self.plotter.add_mesh(mesh_object.polydata,point_size = 1 ,scalars = "color_by",rgb = mesh_object.rgb_status)
            else:
                return self.plotter.add_mesh(mesh_object.polydata,point_size = 1 ,cmap = mesh_object.cmap)
            print("hello")
        else:
            if mesh_object.cmap is  None:
                return self.plotter.add_mesh(mesh_object.polydata,point_size = 1 ,scalars = "color_by",rgb = mesh_object.rgb_status)
            else:
                print("CMAP initiated",)
                return self.plotter.add_mesh(mesh_object.polydata,point_size = 1 ,cmap =  mesh_object.cmap)
#            return self.plotter.add_mesh(mesh_object.polydata,scalars = "color_by",rgb = mesh_object.rgb_status)


