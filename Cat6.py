import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView

class MyWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setHtml('''
        <html>
        <head>
            <title>ทดสอบ</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <hr />
            <p>ทดสอบการแสดงผล HTML ใน QWebEngineView</p>
        </body>
        </html>
        ''')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = MyWeb()
    web.show()
    sys.exit(app.exec())