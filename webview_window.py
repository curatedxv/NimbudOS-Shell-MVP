import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from custom_webview import CustomWebView

class WebViewWindow(QWidget):
    def __init__(self, url: str = "https://example.com"):
        super().__init__()
        self.setWindowTitle("Nimbus WebView")
        self.resize(1200, 800)

        layout = QVBoxLayout(self)
        self.web_view = CustomWebView(url)
        layout.addWidget(self.web_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WebViewWindow("https://boosteroid.com/")
    win.show()
    sys.exit(app.exec_())
