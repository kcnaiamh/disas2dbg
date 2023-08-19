#!/usr/bin/env python3
import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow("Address Converter")
    window.setMinimumWidth(600)
    # window.setMinimumHeight(400)
    # window.setMaximumWidth(600)
    # window.setMaximumHeight(400)
    window.show()
    app.exec()
