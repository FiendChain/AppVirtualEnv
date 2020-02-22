from PySide2 import QtGui, QtCore, QtWidgets

from .InstanceFactoryEditor import InstanceFactoryEditor

class InstanceFactoryListWidget(QtWidgets.QTableWidget):
    def __init__(self, parent, instance_factory_list):
        super().__init__(parent=parent)
        self.instance_factory_list = instance_factory_list

        self.setColumnCount(6)
        self.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.setHorizontalHeaderLabels(["Name", "Env", "Profile", "", "", ""])

        self.update_table()
        self.sortItems(0, QtCore.Qt.AscendingOrder)
        self.instance_factory_list.changed.connect(self.update_table)
    
    def update_table(self):
        self.setSortingEnabled(False)
        self.setRowCount(len(self.instance_factory_list))
        for row, instance in enumerate(self.instance_factory_list):
            self.set_instance(row, instance)
        self.setSortingEnabled(True)

    def set_instance(self, row, instance):
        self.setItem(row, 0, QtWidgets.QTableWidgetItem(instance.name))
        self.setItem(row, 1, QtWidgets.QTableWidgetItem(instance.env_name))
        self.setItem(row, 2, QtWidgets.QTableWidgetItem(instance.username))

        start_button = QtWidgets.QPushButton("Launch")
        start_button.clicked.connect(self.listen_instance_launched(instance))
        self.setCellWidget(row, 3, start_button)

        edit_button = QtWidgets.QPushButton("Edit")
        edit_button.clicked.connect(self.listen_instance_edit(row, instance))
        self.setCellWidget(row, 4, edit_button)

        remove_button = QtWidgets.QPushButton("Remove")
        remove_button.clicked.connect(self.listen_instance_removed(row, instance))
        self.setCellWidget(row, 5, remove_button)

    def listen_instance_edit(self, row, instance):
        def saved_callback(new_instance):
            self.instance_factory_list[row] = new_instance

        def callback():
            window = InstanceFactoryEditor(instance)
            window.setWindowModality(QtCore.Qt.ApplicationModal)
            window.setWindowTitle("Editing Application")
            window.show()
            self.window = window
            self.window.saved.connect(saved_callback)
        return callback

    def listen_instance_removed(self, row, instance):
        def callback():
            reply = QtWidgets.QMessageBox.question(
                self, 
                "Remove Application", 
                "Are you sure you want to remove this application?", 
                QtWidgets.QMessageBox.Yes,
                QtWidgets.QMessageBox.No)
            
            if reply == QtWidgets.QMessageBox.Yes:
                self.instance_factory_list.remove(instance)

        return callback
    
    def listen_instance_launched(self, instance):
        def callback():
            process = instance.create_instance()
            print(process.pid)
        return callback
