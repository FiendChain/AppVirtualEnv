from PySide2 import QtGui, QtCore, QtWidgets

from .InstanceFactoryListWidget import InstanceFactoryListWidget
from .InstanceFactoryCreator import InstanceFactoryCreator

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.setWindowTitle("Application Launcher")
        self.setCentralWidget(self.create_central_widget())

        add_action = self.menuBar().addAction("Add Program")
        add_action.triggered.connect(lambda x: self.on_create_instance())
    
    def create_central_widget(self):
        widget = QtWidgets.QSplitter()

        widget.addWidget(self.create_left_panel())

        return widget

    def create_left_panel(self):
        factory_list = InstanceFactoryListWidget(self, self.app.instance_factory_list)

        return factory_list

        # group = QtWidgets.QGroupBox("Applications")
        # layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(factory_list)
        # group.setLayout(layout)

        # return group

    
    def on_create_instance(self):
        window = InstanceFactoryCreator()
        window.setWindowModality(QtCore.Qt.ApplicationModal)
        window.setWindowTitle("Creating Application")
        window.show()
        self.window = window
        self.window.created.connect(self.add_instance)
    
    def add_instance(self, instance):
        self.app.instance_factory_list.append(instance)

