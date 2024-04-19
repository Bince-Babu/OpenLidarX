from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QCheckBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from pyvistaqt import MainWindow

class TreeWidget(QTreeWidget):
    def __init__(self,signals):
        super().__init__()
        self.signals = signals
        self.itemChanged.connect(self.on_item_changed)
        self.itemClicked.connect(self.on_item_clicked)
        self.setObjectName("TreeWidget")
        self.setEnabled(True)
        self.setHeaderLabel("DB Tree")
        self.setStyleSheet("""
                           QTreeWidget {
                           border-radius:8px;
                           }
            QHeaderView::section {
            font-family: Palatino Linotype;
            font-size: 12pt;
            font-weight: regular;
            border-radius:8px;
            background-color: #333; /* Background color */
            color: white; /* Text color */
            padding-left: 20px; /* Padding around the text */
        }
                           QTreeWidget::item {
                
                            
                            font-size: 12pt;
                            font-weight: regular;
                           }
    """)
    def on_item_changed(self,item,column):
        if item.checkState(column) == Qt.Checked:
            self.signals.add_mesh_signal.emit(item.mesh_object)
        else:
            self.signals.remove_mesh_signal.emit(item.mesh_object)
    def on_item_clicked(self,item,column):
        print(f"Item clicked: {item.text(column)}")
        try:

            self.signals.dbtree_select_signal.emit(item.mesh_object)
        except:
            print("No mesh object")
    def update_tree_widget(self,mesh_object):
        item_0 = QTreeWidgetItem(None)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui/static/open-folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon)
        
        item_0.setText(0,mesh_object.folder_name)
        
        
        #item_0.setCheckState(0, Qt.Unchecked)
        item_1 = QTreeWidgetItem(item_0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("gui/static/cloud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0,icon1)
        item_1.mesh_object = mesh_object
        item_1.setText(0,mesh_object.file_name)
        item_1.setCheckState(0, Qt.Checked)
        self.insertTopLevelItem(0,item_0)
        item_0.setExpanded(True)

