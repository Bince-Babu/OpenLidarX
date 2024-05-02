from PyQt5.QtCore import QObject, pyqtSignal

class Signals(QObject):
    file_dialog_triggered = pyqtSignal()
    registration_triggered = pyqtSignal()
    add_mesh_signal = pyqtSignal(QObject)
    update_mesh_signal = pyqtSignal(QObject) 
    remove_mesh_signal = pyqtSignal(QObject)
    clear_plotter_signal = pyqtSignal()
    point_picking_signal_enable = pyqtSignal()
    point_picking_signal_disable = pyqtSignal()
    distance_measure_enable = pyqtSignal()
    distance_measure_disable = pyqtSignal()
    view_change_signal = pyqtSignal(str)
    dbtree_select_signal = pyqtSignal(QObject)
    downsample_enable = pyqtSignal()
    downsample_disable = pyqtSignal()
    angle_calc_enable = pyqtSignal()
    angle_calc_disable = pyqtSignal()
    clipping_enable=pyqtSignal()
    clipping_disable=pyqtSignal()
    instance_segmentation_signal=pyqtSignal()
    ground_filtering_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        