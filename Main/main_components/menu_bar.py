from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from main_components.Signals import Signals
class Menu_bar:
    def __init__(self,view,menu_bar,signals):
    #def __init__(self,view,menu_bar):
        self.menu_bar = menu_bar
        self.view = view
        self.signals = signals
        self.file_menu = menu_bar.addMenu("File")
        self.tool_menu = menu_bar.addMenu("Tools")
        self.view_menu = menu_bar.addMenu("Views")

        self.add_file_open_menu()
        self.add_registration_menu()
        self.add_point_picking()
        self.add_distance_measure()
        self.add_views()
        self.add_voxel_downsampling()
        self.add_ground_filtering()
        self.add_angle_calc()
        self.add_clipping()
        self.add_instance_segmentation()
    def add_voxel_downsampling(self):
        self.downsample = self.tool_menu.addMenu("Voxel Downsampling")
        self.downsample.setIcon(QIcon("gui/static/cloud_decimate.png"))
        self.downsample.setEnabled(False)
        action_enable=self.downsample_action_enable = QAction(QIcon("gui/static/cloud_decimate.png"), "Enable",self.downsample)
        action_disable=self.downsample_action_disable = QAction(QIcon("gui/static/cloud_decimate.png"), "Disable",self.downsample)
        self.downsample_action_enable.triggered.connect(self.signals.downsample_enable.emit)
        self.downsample_action_disable.triggered.connect(self.signals.downsample_disable.emit)
        self.downsample.addAction(self.downsample_action_enable)
        self.downsample.addAction(self.downsample_action_disable)
    def add_views(self):
        self.right_view_action = QAction(QIcon("gui/static/right-view.png"), "Right View", self.view_menu)
        self.right_view_action.triggered.connect(lambda: self.signals.view_change_signal.emit("R"))
        self.view_menu.addAction(self.right_view_action)

        self.left_view_action = QAction(QIcon("gui/static/left-view.png"), "Left View", self.view_menu)
        self.left_view_action.triggered.connect(lambda: self.signals.view_change_signal.emit("L"))
        self.view_menu.addAction(self.left_view_action)

        self.top_view_action = QAction(QIcon("gui/static/top-view.png"), "Top View", self.view_menu)
        self.top_view_action.triggered.connect(lambda: self.signals.view_change_signal.emit("T"))
        self.view_menu.addAction(self.top_view_action)

        self.bottom_view_action = QAction(QIcon("gui/static/bottom-view.png"), "Bottom View", self.view_menu)
        self.bottom_view_action.triggered.connect(lambda: self.signals.view_change_signal.emit("B"))
        self.view_menu.addAction(self.bottom_view_action)

        self.front_view_action = QAction(QIcon("gui/static/front-view.png"), "Front View", self.view_menu)
        self.front_view_action.triggered.connect(lambda: self.signals.view_change_signal.emit("F"))
        self.view_menu.addAction(self.front_view_action)

        self.back_view_action = QAction(QIcon("gui/static/back-view.png"), "Back View", self.view_menu)
        self.back_view_action.triggered.connect(lambda: self.signals.view_change_signal.emit("Ba"))
        self.view_menu.addAction(self.back_view_action)

        self.front_iso_view_action = QAction(QIcon("gui/static/front-iso.png"), "Front Isometric View", self.view_menu)
        self.front_iso_view_action.triggered.connect(lambda: self.signals.view_change_signal.emit("Fiso"))
        self.view_menu.addAction(self.front_iso_view_action)

        self.back_iso_view_action = QAction(QIcon("gui/static/back-iso.png"), "Back Isometric View", self.view_menu)
        self.back_iso_view_action.triggered.connect(lambda: self.signals.view_change_signal.emit("Biso"))
        self.view_menu.addAction(self.back_iso_view_action)
    def add_file_open_menu(self):
        self.file_open_action = QAction(QIcon("gui/static/open-folder.png"), "Open", self.file_menu)
        self.file_open_action.triggered.connect(self.signals.file_dialog_triggered.emit)
        self.file_menu.addAction(self.file_open_action)
    def add_point_picking(self):
        self.point_pick = self.tool_menu.addMenu("Point Picker")
        self.point_pick.setIcon(QIcon("gui/static/point_pick.png"))
        self.point_pick.setEnabled(False)
        action_enable=self.point_picking_action_enable = QAction(QIcon("gui/static/point_pick.png"), "Enable",self.point_pick)
        action_disable=self.point_picking_action_disable = QAction(QIcon("gui/static/point_pick.png"), "Disable",self.point_pick)
        self.point_picking_action_enable.triggered.connect(self.signals.point_picking_signal_enable.emit)
        self.point_picking_action_disable.triggered.connect(self.signals.point_picking_signal_disable.emit)
        self.point_pick.addAction(self.point_picking_action_enable)
        self.point_pick.addAction(self.point_picking_action_disable)

    def add_distance_measure(self):
        self.distance = self.tool_menu.addMenu("Distance Measurement")
        self.distance.setIcon(QIcon("gui/static/distance.png"))
        self.distance.setEnabled(False)
        action_enable=self.distance_measure_action_enable = QAction(QIcon("gui/static/distance.png"), "Enable",self.distance)
        action_disable=self.distance_measure_action_disable = QAction(QIcon("gui/static/distance.png"), "Disable",self.distance)
        self.distance_measure_action_enable.triggered.connect(self.signals.distance_measure_enable.emit)
        self.distance_measure_action_disable.triggered.connect(self.signals.distance_measure_disable.emit)
        self.distance.addAction(self.distance_measure_action_enable)
        self.distance.addAction(self.distance_measure_action_disable)
    def add_ground_filtering(self):
        self.ground_filtering_action = QAction(QIcon("gui/static/registration_icon.jpeg"),"Ground Filtering",self.tool_menu)
        self.ground_filtering_action.triggered.connect(self.signals.ground_filtering_signal.emit)
        self.tool_menu.addAction(self.ground_filtering_action)

    def add_registration_menu(self):
        self.registation_action = QAction(QIcon("gui/static/registration_icon.jpeg"),"Registration",self.file_menu)
        self.registation_action.triggered.connect(self.signals.registration_triggered.emit)
        self.file_menu.addAction(self.registation_action)
    def add_angle_calc(self):
        self.angle = self.tool_menu.addMenu("Angle Calculation")
        self.angle.setIcon(QIcon("gui/static/angle.png"))
        self.angle.setEnabled(False)
        action_enable=self.angle_calc_action_enable = QAction(QIcon("gui/static/distance.png"), "Enable",self.distance)
        action_disable=self.angle_calc_action_disable = QAction(QIcon("gui/static/distance.png"), "Disable",self.distance)
        self.angle_calc_action_enable.triggered.connect(self.signals.angle_calc_enable.emit)
        self.angle_calc_action_disable.triggered.connect(self.signals.angle_calc_disable.emit)
        self.angle.addAction(self.angle_calc_action_enable)
        self.angle.addAction(self.angle_calc_action_disable)
    def add_clipping(self):
        # self.clip=self.tool_menu.addMenu("Clipping")
        # self.clip.setIcon(QIcon("gui/static/clipping.jpg"))
        # action_enable=self.clip_action_enable=QAction(QIcon("gui/static/distance.png"), "Enable",self.distance)
        # action_disable=self.clip_action_disable = QAction(QIcon("gui/static/distance.png"), "Disable",self.distance)
        # self.clip_action_enable.triggered.connect(self.signals.clipping_enable.emit)
        # self.clip_action_disable.triggered.connect(self.signals.clipping_disable.emit)
        # self.clip.addAction(self.clip_action_enable)
        # self.clip.addAction(self.clip_action_disable)
        self.clipping_action=QAction(QIcon("gui/static/clipping.jpg"),"Clipping",self.tool_menu)
        self.clipping_action.triggered.connect(self.signals.clipping_signal.emit)
        self.tool_menu.addAction(self.clipping_action)
    def add_instance_segmentation(self):
        self.instance_segmentation_action = QAction(QIcon("gui/static/instance_Segmentation.png"),"Instance Segmentation",self.tool_menu)
        self.instance_segmentation_action.triggered.connect(self.signals.instance_segmentation_signal.emit)
        self.tool_menu.addAction(self.instance_segmentation_action)
