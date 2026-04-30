import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class myApp(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(320, 240)  # กำหนดขนาดของหน้าต่างโปรแกรม
        self.setWindowTitle("Hello, World!")  # กำหนดชื่อหัวโปรแกรม

        layout = QVBoxLayout()
        self.setLayout(layout)

        hello = QPushButton("Hello world!")  # ข้อความในปุ่ม
        hello.resize(100, 30)  # กำหนดขนาดของปุ่ม

        layout.addWidget(hello)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())