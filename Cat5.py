import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView


class MyWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.load(QUrl("https://www.youtube.com"))  # โหลดเว็บ


if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = MyWeb()
    web.show()
    sys.exit(app.exec())