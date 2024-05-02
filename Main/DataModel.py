import laspy
import pyvista as pv
import numpy as np
from Mesh import Mesh
import open3d as o3d
import laspy
from PyQt5.QtCore import QThread
import gc
class DataModel:
    def __init__(self):
        print("Object of the data model created")
    
    def file_process(self,file_name):
        self.return_value = None
        self.file_name = file_name
        file_extension = file_name.split(".")[-1].lower()
        if file_extension == "pcd":
            return self.process_pcd_file()
        elif file_extension == "las":
            return self.process_las_file()
    def process_pcd_file(self):
        pcd = o3d.io.read_point_cloud(self.file_name)
        mesh_object = Mesh()
        mesh_object.add_file_name(self.file_name)
        # np_colors = np.asarray(pcd.colors)
        # np_colors = (np_colors * 255).astype(np.uint8)
        # print("HWllo",np_colors)
        points_np = np.asarray(pcd.points)
        mesh_object.add_point_data(points_np)
        #mesh_object.add_color_data(np.ones((points_np.shape[0],3)))
        #mesh_object.add_color_data(np.full((points_np.shape[0], 3),0))
        mesh_object.add_color_data(np.random.rand(points_np.shape[0], 3))
        mesh_object.rgb_status = True
        self.return_value = mesh_object
        return mesh_object
    def process_las_file(self):
        las_file = laspy.read(self.file_name)
        mesh_object = Mesh()
        mesh_object.add_file_name(self.file_name)
        points = np.vstack((las_file.X,las_file.Y,las_file.Z)).transpose()
        random_numbers = np.random.randint(0, points.shape[0], size=6000000)
        points = points[random_numbers]
        mesh_object.add_point_data(points)
        # for name in las_file.point_format.dimension_names:
        #     print(name)
        # if "red" in las_file.point_format.dimension_names and "green" in las_file.point_format.dimension_names and "blue" in las_file.point_format.dimension_names:
        try:
            color_values = np.vstack((las_file.red,las_file.green,las_file.blue)).transpose()
            color_values = color_values[random_numbers]
            color_values = color_values/65335
            mesh_object.rgb_status = True
        
        except:
            print("Color information is not included in the las file")
            mesh_object.rgb_status = False
            color_values = points[:,2]
            color_values = color_values/np.max(color_values)
            mesh_object.rgb_status = False
            print("Color values",color_values)
        finally:
            mesh_object.add_color_data(color_values)
        worker = Worker(points)
        worker.start()
        worker.wait()
        # mesh_object.add_point_data(points)
        # mesh_object.add_color_data(points[:,2])
        #mesh_object.add_color_data( np.random.rand(276357, 3))
        #del las_file
        #gc.collect()
        return mesh_object


class Worker(QThread):
    def __init__(self,points):
        super().__init__()
        self.points  = points
    def run(self):
        k = 0
        for i in self.points:
            k = k+1 
        print("kkkkk",k)














    # def load_las_file(self, file_path):   # should return a object of the Mesh class created
    #     las_file = laspy.read(file_path)
    #     x = las_file.X.astype(np.float32)
    #     y = las_file.Y.astype(np.float32)
    #     z = las_file.Z.astype(np.float32)
    #     points = np.vstack((x, y, z)).transpose()
    #     self.point_cloud = pv.PolyData(points)
    # def load_las_file(self,file_path):   # should return a object of the Mesh class created
    #     plydata = PlyData.read('sample.ply')
    #     for point in plydata['vertex']:
    #         red = point['red']
    #         green = point['green']
    #         blue = point['blue']
    #         print(f'Red: {red}, Green: {green}, Blue: {blue}')
    # def load_pcd_file(self,file_path):    # should return a object of the Mesh class created
    #     #print("file",file_path)
    #     pcd = o3d.io.read_point_cloud(file_path)
    #     new_mesh = Mesh(pcd.points,pcd.colors)
    #     #include code to add various information in the each file
    #     return new_mesh
    # def get_point_cloud(self):
    #     return self.main_poly_data