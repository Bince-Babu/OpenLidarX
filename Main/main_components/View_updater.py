class View_updater:
    def __init__(self,plotter):
        self.plotter = plotter
        print("View Updater initiated")
    def update_view(self,view):
        
        if view == 'F':
            self.plotter.camera.azimuth = 180
            self.plotter.camera_position = "xz"

        elif view == 'Ba':
            self.plotter.camera.roll = 0 
            self.plotter.camera_position = "yx"

        elif view == "Biso":
            self.plotter.camera_position = "iso"

        elif view == 'Fiso':
            self.plotter.camera_position = "iso"
            self.plotter.camera.azimuth = 180
            

        elif view == 'L':
            self.plotter.camera.azimuth = 180
            self.plotter.camera_position = "yz"
            
        elif view == 'R':
            self.plotter.camera.azimuth = 0
            self.plotter.camera_position = "yz"


        elif view == "T":
            self.plotter.camera_position = "xy"

        #requires change in back_view
        elif view == "B":
            self.plotter.camera_position = "yx"
            self.plotter.camera.roll = 0
            