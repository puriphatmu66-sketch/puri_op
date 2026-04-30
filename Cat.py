import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel("<font color=red size=40>Hello World</font>")
label = QLabel("Hello World")
label.resize(800, 540)
label.setWindowTitle("Hello, MY!")
label.show()

app.exec()