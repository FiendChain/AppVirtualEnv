from PySide2 import QtGui, QtCore, QtWidgets
import os

from models import InstanceFactory

class InstanceFactoryWidget(QtWidgets.QWidget):
    def __init__(self, instance=InstanceFactory(), parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle("Edit Options")
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Maximum,
            QtWidgets.QSizePolicy.Expanding) 

        layout = QtWidgets.QGridLayout()

        self.name_field = QtWidgets.QLineEdit(instance.name)
        layout.addWidget(QtWidgets.QLabel("Name:"), 0, 0)
        layout.addWidget(self.name_field, 0, 1, 1, 2)

        self.exec_path_field = QtWidgets.QLineEdit(instance.exec_path)
        self.exec_browse_button = QtWidgets.QPushButton("&Browse...", self)
        self.exec_browse_button.clicked.connect(self.browse_exec_path)
        layout.addWidget(QtWidgets.QLabel("Exec:"), 1, 0)
        layout.addWidget(self.exec_path_field, 1, 1, 1, 1)
        layout.addWidget(self.exec_browse_button, 1, 2, 1, 1)

        self.args_field = QtWidgets.QLineEdit(instance.args)
        layout.addWidget(QtWidgets.QLabel("Args:"), 2, 0)
        layout.addWidget(self.args_field, 2, 1, 1, 2)

        self.username_field = QtWidgets.QLineEdit(instance.username)
        layout.addWidget(QtWidgets.QLabel("Username:"), 3, 0)
        layout.addWidget(self.username_field, 3, 1, 1, 2)

        self.env_name_field = QtWidgets.QLineEdit(instance.env_name)
        layout.addWidget(QtWidgets.QLabel("Env:"), 4, 0)
        layout.addWidget(self.env_name_field, 4, 1, 1, 2)

        self.env_config_path_field = QtWidgets.QLineEdit(instance.env_config_path)
        self.env_config_browse_button = QtWidgets.QPushButton("&Browse...", self)
        self.env_config_browse_button.clicked.connect(self.browse_config_path)
        layout.addWidget(QtWidgets.QLabel("Config:"), 5, 0)
        layout.addWidget(self.env_config_path_field, 5, 1, 1, 1)
        layout.addWidget(self.env_config_browse_button, 5, 2, 1, 1)

        self.env_parent_dir_field = QtWidgets.QLineEdit(instance.env_parent_dir)
        self.env_parent_dir_browse_button = QtWidgets.QPushButton("&Browse...", self)
        self.env_parent_dir_browse_button .clicked.connect(self.browse_env_parent_dir)
        layout.addWidget(QtWidgets.QLabel("Location:"), 6, 0)
        layout.addWidget(self.env_parent_dir_field, 6, 1, 1, 1)
        layout.addWidget(self.env_parent_dir_browse_button, 6, 2, 1, 1)

        self.setLayout(layout)
    
    def browse_exec_path(self):
        cwd = QtCore.QDir.currentPath()
        filepath, ext = QtWidgets.QFileDialog.getOpenFileName(
            self, 
            "Find Executable", 
            cwd,
            ";;".join(["Executable (*.exe)", "All (*)"]))
        if filepath:
            filepath = os.path.realpath(filepath)
            self.exec_path_field.setText(filepath)

    def browse_config_path(self):
        cwd = QtCore.QDir.currentPath()
        filepath, ext = QtWidgets.QFileDialog.getOpenFileName(
            self, 
            "Find Environment Configuration",
            cwd,
            ";;".join(["JSON (*.json)", "All (*)"]))

        if filepath:
            filepath = os.path.realpath(filepath)
            self.env_config_path_field.setText(filepath)

    def browse_env_parent_dir(self):
        cwd = QtCore.QDir.currentPath()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Directory", cwd)
        if directory:
            directory = os.path.realpath(directory)
            self.env_parent_dir_field.setText(directory)

    def create_instance_factory(self):
        instance = InstanceFactory()
        instance.name = self.name_field.text()
        instance.username = self.username_field.text()
        instance.exec_path = self.exec_path_field.text()
        instance.args = self.args_field.text()
        instance.env_name = self.env_name_field.text()
        instance.env_config_path = self.env_config_path_field.text()
        instance.env_parent_dir = self.env_parent_dir_field.text()

        return instance
