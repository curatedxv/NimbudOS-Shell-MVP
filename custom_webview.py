from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class CustomWebView(QWebEngineView):
    def __init__(self, url: str = None):
        super().__init__()
        self.settings().setAttribute(self.settings().JavascriptEnabled, True)
        self.settings().setAttribute(self.settings().PluginsEnabled, True)
        if url:
            self.load(QUrl(url))
