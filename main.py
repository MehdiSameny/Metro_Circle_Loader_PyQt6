# ///////////////////////////////////////////////////////////////
# Developer: Mehdi Sameni
# Designer: Mehdi Sameni
# PyQt6
# Python 3.10
# other module : perlin_noise
# ///////////////////////////////////////////////////////////////

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QColor
from MetroCircleLoader import MetroCircleProgress



class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(MetroCircleProgress(self))

        layout.addWidget(MetroCircleProgress(self, radius=10))

        layout.addWidget(MetroCircleProgress(self, styleSheet="""qproperty-color: rgb(255, 0, 0);"""))

        layout.addWidget(MetroCircleProgress(self, styleSheet="""qproperty-color: rgb(0, 0, 255);
                                                        qproperty-backgroundColor: rgba(180, 180, 180, 180);"""))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
