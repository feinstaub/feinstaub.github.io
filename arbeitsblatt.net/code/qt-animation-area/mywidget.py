from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QFont, QColor, QPen, QCursor, QPixmap
from PyQt5.QtCore import Qt, QTimer
import math

#
# Weitere Ideen siehe auch:
#  - http://interactivepython.org/courselib/static/everyday/2013/05/1_processing.html
#
class MyWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setMinimumSize(1, 30)
        self.setFocusPolicy(Qt.StrongFocus) # to be able to accept key events

        self.paint_image = QPixmap(self.width(), self.height())
        self.background_color = QColor(70, 70, 70)

        self.fps = 30
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrame)
        self.timer.start(1000 / 30)

        self.frame_count = 0
        self.x1 = 50
        self.y1 = 50
        self.radius1 = 50

        self.color2 = QColor(0, 0, 255)
        self.x2 = 50
        self.y2 = 50
        self.angle2 = 20


    def setFrameRate(self, fps):
        self.fps = fps
        if self.fps > 0:
            if not self.timer.isActive():
                self.timer.start()
            self.timer.setInterval(1000 / self.fps)
        else:
            self.timer.stop()

    def nextFrame(self):
        mouse_pos = self.mapFromGlobal(QCursor.pos())
        mouse_x = mouse_pos.x()
        mouse_y = mouse_pos.y()

        self.x1 = mouse_x
        self.y1 = mouse_y
        self.radius1 = self.radius1 + math.sin(self.frame_count / 8) * 4

        delay = 20
        self.x2 += (mouse_x - self.x2) / delay
        self.y2 += (mouse_y - self.y2) / delay

        self.frame_count += 1

        if self.paint_image.width() != self.width() or self.paint_image.height() != self.height():
            self.paint_image = QPixmap(self.width(), self.height())
            self.paint_image.fill(self.background_color)

        p = QPainter()
        p.begin(self.paint_image) # auf das paint_image malen
        p.setBackground(self.background_color) # color when stuff is erased

        # Hintergrund löschen, wenn Rechteck bei der Maus angekommen ist
        # print("{0}, {1}".format(self.x2, mouse_x))
        if round(self.x2) == mouse_x and round(self.y2) == mouse_y:
            p.eraseRect(0, 0, self.paint_image.width(), self.paint_image.height())

        self.drawFrame(p)
        p.end()
        self.repaint()

    def drawFrame(self, p):
        pen = QPen(QColor(20, 20, 20), 10, Qt.SolidLine)
        p.setPen(pen)

        x1 = self.x1 - self.radius1 / 2
        y1 = self.y1 - self.radius1 / 2
        p.drawEllipse(x1, y1, self.radius1, self.radius1)

        pen = QPen(self.color2, 5, Qt.SolidLine) # blau
        p.setPen(pen)
        w2 = 50

        # see https://www.khanacademy.org/computing/computer-programming/programming-games-visualizations/programming-transformations/a/rotation
        p.save()
        p.translate(self.x2, self.y2)
        p.rotate(self.angle2) # todo keypress
        p.drawRect(0, 0, w2, w2)
        p.restore()

    def paintEvent(self, e):

        p = QPainter()
        p.begin(self)

        # self.drawFrame(p) # Frame direkt malen (ohne paint_image)

        p.drawPixmap(0, 0, self.paint_image)
        p.end()

    def keyPressEvent(self, e):
        print(e.key(), e.text())
        if e.key() == Qt.Key_Left:
            self.angle2 -= 10
        elif e.key() == Qt.Key_Right:
            self.angle2 += 10

        if e.key() == Qt.Key_P:
            print("P pressed")

        if e.key() == Qt.Key_C:
            print("C pressed")
            if self.color2 == QColor(0, 0, 255):
                self.color2 = QColor(0, 255, 0)
            else:
                self.color2 = QColor(0, 0, 255)

    def mousePressEvent(self, e):
        print(e.x(), e.y())

        p = QPainter()
        p.begin(self.paint_image) # auf das paint_image malen
        self.drawOnClick(e, p)
        p.end()
        self.repaint()

    def drawOnClick(self, e, p):
        pen = QPen(QColor(255, 0, 0), 20, Qt.SolidLine, Qt.RoundCap)
        p.setPen(pen)
        p.drawPoint(e.x(), e.y())

