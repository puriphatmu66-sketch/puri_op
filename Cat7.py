import os
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import sys

class myWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        
        # 1. กำหนดตำแหน่งไฟล์รูป
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "pp.png")
        
        # 2. เขียน HTML โดยใช้ชื่อไฟล์ตรงๆ (ไม่ต้องใส่ path เต็มใน src ถ้ากำหนด baseUrl แล้ว)
        html_content = f"""
        <html>
        <body style="margin:0;">
            <img src="pp.png" width="100%">
        </body>
        </html>
        """
        
        # 3. หัวใจสำคัญ: ใส่ QUrl.fromLocalFile(current_dir) เป็น Argument ตัวที่สอง
        self.setHtml(html_content, QUrl.fromLocalFile(current_dir + os.path.sep))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = myWeb()
    web.show()
    sys.exit(app.exec())