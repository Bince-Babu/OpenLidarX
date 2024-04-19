from PyQt5.QtCore import QObject
class PolyDataController(QObject):
    def __init__(self,view):
        super().__init__()
        self.view = view
        self.mesh_objects = None
    def handle_mesh_objects(self,mesh_objects):
        self.mesh_objects = mesh_objects

    def convert_to_polydata(self):



