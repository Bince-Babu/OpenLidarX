from PyQt5.QtWidgets import QFileDialog
from DataModel import DataModel
# This will open a file dialog and return the selected file paths as a list of strings
def file_handle_window():
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("LAS, PCD, LAZ, XYZ Files (*.las *.pcd *.laz *.xyz)")
        file_dialog.setWindowTitle("Open Point Cloud File")
        #print("File opening triggered")

        if file_dialog.accepted:
             file_paths, _ = file_dialog.getOpenFileNames()
        #file_paths = ["C:/Users/babub/open3d_data/extract/DemoICPPointClouds/cloud_bin_0.pcd","C:/Users/babub/open3d_data/extract/DemoICPPointClouds/cloud_bin_1.pcd"]
        #file_paths = ["C:/Users/babub/open3d_data/extract/DemoICPPointClouds/cloud_bin_0.pcd","C:/Users/babub/open3d_data/extract/DemoICPPointClouds/cloud_bin_1.pcd","C:/Users/babub/open3d_data/extract/DemoICPPointClouds/cloud_bin_2.pcd"]
        
        #file_paths = ["C:/Users/babub/open3d_data/extract/DemoICPPointClouds/cloud_bin_0.pcd"]  
        #file_paths = ["D:/cubes.las"]
        #file_paths = ["D:\pointcloud.las"]
        #file_paths = ["D:/kalyan.las"]
        model_creator = DataModel()
        
        mesh_objects = [model_creator.file_process(file) for file in file_paths]
        return mesh_objects