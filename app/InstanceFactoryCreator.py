from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import QObject, Property, Slot, Signal

from models import InstanceFactory, Observable
from .InstanceFactoryWidget import InstanceFactoryWidget

class InstanceFactoryCreator(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.created = Observable()

        layout = QtWidgets.QVBoxLayout()

        self.editor = InstanceFactoryWidget(parent=self)
        layout.addWidget(self.editor) 

        self.button = QtWidgets.QPushButton("Create", self)
        self.button.clicked.connect(self.on_create)
        layout.addWidget(self.button)

        self.setLayout(layout)
    
    def on_create(self):
        instance = self.editor.create_instance_factory()
        self.created.emit(instance)
        self.close()