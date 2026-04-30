import sys
from PySide6.QtWidgets import *


class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(320, 240)  # กำหนดขนาดของหน้าต่างโปรแกรม
        self.setWindowTitle("Hello, World!")  # กำหนดชื่อหัวโปรแกรม

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Hello World")
        label_Cat4 = QLabel("1145 006 Object-Oriented Programming 62")
        label2 = QLabel("สวัสดี")
        label3 = QLabel("เพิ่มเริ่มต้น เรียน PySide")

        layout.addWidget(label)
        layout.addWidget(label_Cat4)
        layout.addWidget(label2)
        layout.addWidget(label3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())