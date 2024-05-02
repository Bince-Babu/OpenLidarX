from PyQt5.QtWidgets import QListWidget, QRadioButton, QListWidgetItem, QVBoxLayout, QDialog, QLineEdit, QHBoxLayout, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from pyvistaqt import MainWindow


class Properties(QListWidget):
    def __init__(self,signals):
        super().__init__()
        self.signals = signals
        
    def update_list_widget(self,mesh_object):
        self.mesh_object = mesh_object
        self.setStyleSheet("""
                           QListWidget {
                           border-radius:8px;
                           margin-top:0;
                           }
            QListWidget::item {
                
                
                font-family: Helvetica;
                font-size: 10pt;
                padding: 5px; /* Padding around the text */
            }
            
        """)
        self.clear()
        no_of_points=mesh_object.polydata.number_of_points
        item_names=[f"Selected File Name: {mesh_object.file_name}",f"Number of points: {mesh_object.polydata.number_of_points}",f"Color By:"]
        self.addItems(item_names)
         


         #       RGB
        radio_button_rgb = QRadioButton("RGB")
        radio_button_elevation = QRadioButton("Elevation")
        radio_button_custom = QRadioButton("Custom Color")

        if mesh_object.rgb_status:
            list_item_rgb = QListWidgetItem()
            self.addItem(list_item_rgb)
            self.setItemWidget(list_item_rgb,radio_button_rgb)

        list_item_elevation = QListWidgetItem()
        self.addItem(list_item_elevation)
        self.setItemWidget(list_item_elevation,radio_button_elevation)


        list_item_custom = QListWidgetItem()
        self.addItem(list_item_custom)
        self.setItemWidget(list_item_custom,radio_button_custom)

        if mesh_object.rgb_status:
            radio_button_rgb.setChecked(True)
        if not mesh_object.rgb_status:
            radio_button_elevation.setChecked(True)
        radio_button_elevation.clicked.connect(self.elevation_triggered)
        radio_button_rgb.clicked.connect(self.rgb_triggered)
        radio_button_custom.clicked.connect(self.show_text_input_dialog)
    def rgb_triggered(self):
        self.mesh_object.cmap = None
        self.mesh_object.set_color_data()
        self.signals.remove_mesh_signal.emit(self.mesh_object)
        self.signals.add_mesh_signal.emit(self.mesh_object)   
    def elevation_triggered(self):
        self.mesh_object.cmap = None
        print("Function triggered")
        self.mesh_object.set_color_elevation()
        self.signals.remove_mesh_signal.emit(self.mesh_object)
        self.signals.add_mesh_signal.emit(self.mesh_object)
    def show_text_input_dialog(self):
        dialog = TextInputDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            input_text = dialog.text_edit.text()
            self.mesh_object.cmap = input_text
            self.signals.remove_mesh_signal.emit(self.mesh_object)
            self.signals.add_mesh_signal.emit(self.mesh_object)
class TextInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.text_edit = QLineEdit()
        layout.addWidget(self.text_edit)
        self.text_edit.setMinimumSize(200, 30) 
        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)
        self.setWindowTitle("Custom Color")
