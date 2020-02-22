from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import QObject, Property, Slot, Signal

from models import InstanceFactory, Observable
from .InstanceFactoryWidget import InstanceFactoryWidget

class InstanceFactoryEditor(QtWidgets.QWidget):

    def __init__(self, instance, parent=None):
        super().__init__(parent=parent)

        self.saved = Observable()

        layout = QtWidgets.QVBoxLayout()

        self.editor = InstanceFactoryWidget(instance=instance, parent=self)
        layout.addWidget(self.editor) 

        self.button = QtWidgets.QPushButton("Save", self)
        self.button.clicked.connect(self.on_save)
        layout.addWidget(self.button)

        self.setLayout(layout)
    
    def on_save(self):
        instance = self.editor.create_instance_factory()
        self.saved.emit(instance)
        self.close()