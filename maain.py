from PyQt5.QtWidgets import QApplication
from gui.MainWindow import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())