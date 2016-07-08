#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Matrix-Draw
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.w = 400
        self.h = 300
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, self.w, self.h)
        self.setWindowTitle('QPainter-Beispiel')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawMatrix(qp)
        qp.end()


    def drawMatrix(self, qp):

        qp.setPen(QPen(Qt.black))

        qp.drawPoint(50, 50)
        qp.drawPoint(0, 0)
        qp.drawPoint(0, 20)
        qp.drawPoint(20, 0)

        y = 10
        for x in range(0, self.w):
             qp.drawPoint(x, y)

        # rot, grün, blau
        qp.setPen(QColor(255, 0, 0))
        y = 30
        for x in range(0, self.w):
            if x > 100 and x < 200:
                qp.drawPoint(x, y)

        y = 40
        qp.setPen(QColor(0, 255, 0))
        for x in range(0, self.w):
            qp.drawPoint(x, y)

        for x in range(0, 255):
            qp.setPen(QColor(0, 0, x))
            qp.drawPoint(x + 50, x)

        for x in range(0, 255):
            qp.setPen(QColor(0, x, 0))
            qp.drawPoint(x + 70, x)

            qp.setPen(QColor(0, 255 - x, x))
            qp.drawPoint(x + 90, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
