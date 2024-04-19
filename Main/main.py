import sys
from PyQt5.QtWidgets import QApplication
from Controller import DataFlowController
from DataModel import DataModel
from View import DataView

if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = DataView()
    model = DataModel()
    controller = DataFlowController(model,view)

    view.show()
    sys.exit(app.exec_())