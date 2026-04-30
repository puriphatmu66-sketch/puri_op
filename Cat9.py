import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

app = QApplication(sys.argv)

quit_btn = QPushButton("Quit")  # ข้อความในปุ่ม
quit_btn.resize(75, 30)          # ขนาดปุ่ม
quit_btn.setFont(QFont("Times", 18, QFont.Bold))

# PySide6 ใช้แบบนี้แทน SIGNAL/SLOT (ของเก่า)
quit_btn.clicked.connect(app.quit)

quit_btn.show()

sys.exit(app.exec())