import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

class myMessageBox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('กล่องข้อความ')  # ชื่อหัวของโปรแกรม

    def closeEvent(self, event):
        # กำหนดการทำงานตอนกดปิดหน้าต่าง
        reply = QMessageBox.question(
            self,
            'Message',
            "คุณแน่ใจนะว่าคุณต้องการปิดโปรแกรม?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()  # ปิดโปรแกรม
        else:
            event.ignore()  # ไม่ปิดโปรแกรม

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qb = myMessageBox()
    qb.show()
    sys.exit(app.exec())