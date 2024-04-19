from PyQt5.QtWidgets import QMainWindow,QHBoxLayout,QVBoxLayout, QWidget, QMenuBar, QAction, QFileDialog,QPushButton,QSplitter,QListWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
from pyvistaqt import QtInteractor
import os
from pyvistaqt import BackgroundPlotter
import pyvista as pv
from main_components.menu_bar import Menu_bar
from main_components.Signals import Signals
from main_components.left_widget import LeftWidget
from PyQt5 import QtWidgets
from main_components.dbtree import TreeWidget
from main_components.Plotter_widgets import PlotterWidget
class DataView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenLidarX")
        self.setMinimumSize(700, 500)
        self.showMaximized() #Required?
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.plotter_widget = PlotterWidget()
        
        self.signals = Signals()
        
        self.signals.file_dialog_triggered.emit()
        main_layout = QHBoxLayout()
        self.plotter_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  #doubt verify again 
        splitter = QSplitter()
        self.left_widget = LeftWidget(self.signals)
        splitter.addWidget(self.left_widget)
        splitter.addWidget(self.plotter_widget)
        splitter.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizes=[150,splitter.width()-150]
        splitter.setSizes(sizes)
        main_layout.addWidget(splitter)
        # Create a central widget and set the main layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)

        self.menu_bar()
    def menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        self.nav_bar = Menu_bar(self,menu_bar,self.signals)