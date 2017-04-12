import sys
from calc.app import CreateApp
from PyQt5.QtWidgets import *


class Application(QWidget):
    """
    Application is the class that initializes the app
    Application inherits from QWidget
    only method is __init__
    CreateApp is called in the init and then the attribute grid on
    CreateApp is passed into setLayout, then self.show()
    is called and displays the app
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Caluclator")
        self.calc_app = CreateApp()
        self.setLayout(self.calc_app.grid)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())
