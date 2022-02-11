from PyQt5.QtWidgets import QDialog, QMessageBox, QMainWindow

import repository
from UI_AuthentificationDialog import UI_AuthentificationDialog
from repository import connect_with_database
from UI_MainMenu import *
from PyQt5 import QtWidgets # import PyQt5 widgets
import sys

class ApplicationData():
    widget = None

if __name__ == '__main__':
    # Create the application object
    app = QtWidgets.QApplication(sys.argv)

    # Create the form object

    #connect_with_database(False)
    widget = QtWidgets.QStackedWidget()

    window = UI_MainMenu(widget)
    widget.addWidget(window)
    #widget.addWidget(edit)
    widget.resize(820, 484)
    widget.show()

    exit(app.exec_())



