from main_components.dbtree import TreeWidget
from main_components.props import Properties
from PyQt5.QtWidgets import QListWidget,QWidget,QVBoxLayout,QLabel
class LeftWidget(QWidget):
    def __init__(self,signals):
        super().__init__()
        self.signals = signals
        self.tree_widget = TreeWidget(self.signals)
        self.list_widget = Properties(self.signals)
        
        # self.list_widget = QListWidget()
        self.left_layout = QVBoxLayout()
        
        self.setLayout(self.left_layout)
        self.left_layout.addWidget(self.tree_widget)
        label = QLabel('Properties:')
        label.setStyleSheet("margin-top:10px;font-family: Palatino Linotype;font-size: 12pt;font-weight: regular;background-color: #333;color: white;padding-left: 20px;border-radius:8px;")
        label.setFixedHeight(50)
        self.left_layout.addWidget(label)
        self.left_layout.addWidget(self.list_widget)
