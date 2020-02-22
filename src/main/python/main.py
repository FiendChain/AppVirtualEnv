import os
import sys
import argparse

from PySide2 import QtGui, QtCore, QtWidgets
from app import MainWindow
from models import App

from fbs_runtime.application_context.PySide2 import ApplicationContext

def main():
    app_context = ApplicationContext()

    parser = argparse.ArgumentParser()
    parser.add_argument("--apps", default="config/apps.json")
    args = parser.parse_args()

    app = App(args)
    window = MainWindow(app)
    window.show()

    app_context.app.setStyle("windowsvista")
    return app_context.app.exec_()

if __name__ == '__main__':
    main()