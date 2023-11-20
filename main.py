import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QPointF
from PyQt5 import uic


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui')

        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin()
            self.drawCircle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def drawCircle(self, qp):
        qp.setBrush(QColor(255, 165, 0))
        r = random.randint(50, 250)
        c = random.randint(20, 300), random.randint(20, 300)
        qp.drawEllipse(QPointF(c), r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())