import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.make_circle.clicked.connect(self.create_circle)
        self.circle_position = None

    def create_circle(self):
        self.circle_position = (
            randint(50, self.width() - 50),
            randint(50, self.height() - 50),
        )
        self.update()

    def paintEvent(self, event):
        if self.circle_position:
            qp = QPainter(self)
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QColor(0, 0, 0))

        x, y = self.circle_position
        radius = randint(1, 200)
        qp.drawEllipse(x - radius, y - radius, radius * 2, radius * 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
