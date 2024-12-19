import sys
import random
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.uic import loadUi


class MainWindow(QtWidgets.QMainWindøow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.draw_circles)
        self.circles = []

    def paintEvent(self, event):
        paint = QtGui.QPainter(self)
        paint.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.yellow))
        for (x, y, d) in self.circles:
            paint.drawEllipse(x, y, d, d)

    def draw_circles(self):
        d = random.randint(20, 100)
        x = random.randint(0, self.width() - d)
        y = random.randint(0, self.height() - d)
        self.circles.append((x, y, d))
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
