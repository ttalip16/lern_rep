import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from math import sqrt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setGeometry(300, 300, 200, 200)
        self.pushButton.clicked.connect(self.re_draw)
        self.is_draw = False

    def paintEvent(self, event):
        if self.is_draw:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()

    def draw(self):
        self.qp.setBrush(QColor(255, 255, 0))
        a = random.randint(10, 100)
        x, y = random.randint(0, 300), random.randint(0, 200)
        self.qp.drawEllipse(x - a // 2, y - a // 2, a, a)

    def re_draw(self):
        self.is_draw = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())