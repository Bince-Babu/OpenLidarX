import open3d as o3d
import numpy as np
import copy
class ICPRegistration():
    def __init__(self,controller):
        print("Object of the ICPRegistration is created")
        self.controller = controller
        
    def do_registration(self,mesh_objects):
        self.o3d_point0 = o3d.geometry.PointCloud()
        self.o3d_point1 = o3d.geometry.PointCloud()
        threshold = 0.02
        try:
            self.o3d_point0.points = o3d.utility.Vector3dVector(mesh_objects[0].point_data)
            self.o3d_point1.points = o3d.utility.Vector3dVector(mesh_objects[1].point_data)
        except:
            print("Currently only two files used fo registrtion")
            return None
        init_transform = np.asarray([[0.862, 0.011, -0.507, 0.5],
                             [-0.139, 0.967, -0.215, 0.7],
                             [0.487, 0.255, 0.835, -1.4], 
                             [0.0, 0.0, 0.0, 1.0]])
        self.point_to_point_icp(self.o3d_point0,self.o3d_point1,threshold,init_transform,mesh_objects)
        self.return_registered_mesh()
    def point_to_point_icp(self,source, target, threshold, trans_init,mesh_objects):
        reg_p2p = o3d.pipelines.registration.registration_icp(source, target, threshold, trans_init,o3d.pipelines.registration.TransformationEstimationPointToPoint())
        self.after_registration(source,target,reg_p2p.transformation,mesh_objects)    
    def after_registration(self,source,target,transformation,mesh_objects):
        self.registered_mesh = mesh_objects[0]
        source_temp = copy.deepcopy(source)
        source_temp.transform(transformation)
        print("TRANSFORMATION COMPLETED")
        self.registered_mesh.add_point_data(np.asarray(source_temp.points),True)
        self.registered_mesh.add_color_data(mesh_objects[0].polydata["color_by"])
        self.registered_mesh.file_name = "Reg " + self.registered_mesh.file_name
        print("REGISTRATION COMPLETED")
    def return_registered_mesh(self):
        return self.registered_mesh

