import sys
import psutil
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QHBoxLayout, QStackedWidget, QLabel, QMessageBox
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt

class NimbusShell(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nimbus Shell MVP")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        self.layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.stacked_widget = QStackedWidget()

        self.btn_docs = QPushButton("Docs")
        self.btn_sheets = QPushButton("Sheets")
        self.btn_slides = QPushButton("Slides")
        self.btn_boosteroid = QPushButton("Boosteroid")
        self.btn_resources = QPushButton("Resources")

        for btn in [self.btn_docs, self.btn_sheets, self.btn_slides, self.btn_boosteroid, self.btn_resources]:
            btn.setStyleSheet("background-color: #333333; padding: 10px; font-size: 16px;")
            self.button_layout.addWidget(btn)

        self.empty_widget = QLabel("Добро пожаловать в Nimbus Shell!\nВыберите сервис сверху.")
        self.empty_widget.setAlignment(Qt.AlignCenter)
        self.stacked_widget.addWidget(self.empty_widget)

        self.web_docs = None
        self.web_sheets = None
        self.web_slides = None
        self.web_boosteroid = None

        self.loader = QLabel("Loading...")
        self.loader.setAlignment(Qt.AlignCenter)
        self.stacked_widget.addWidget(self.loader)

        self.btn_docs.clicked.connect(lambda: self.show_service("docs"))
        self.btn_sheets.clicked.connect(lambda: self.show_service("sheets"))
        self.btn_slides.clicked.connect(lambda: self.show_service("slides"))
        self.btn_boosteroid.clicked.connect(lambda: self.show_service("boosteroid"))
        self.btn_resources.clicked.connect(self.show_resources)

        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.stacked_widget)
        self.setLayout(self.layout)

    def show_service(self, service_name):
        self.stacked_widget.setCurrentWidget(self.loader)

        if service_name == "docs":
            if not self.web_docs:
                self.web_docs = QWebEngineView()
                self.web_docs.load(QUrl("https://docs.google.com/document/u/0/"))
                self.stacked_widget.addWidget(self.web_docs)
            self.stacked_widget.setCurrentWidget(self.web_docs)

        elif service_name == "sheets":
            if not self.web_sheets:
                self.web_sheets = QWebEngineView()
                self.web_sheets.load(QUrl("https://docs.google.com/spreadsheets/u/0/"))
                self.stacked_widget.addWidget(self.web_sheets)
            self.stacked_widget.setCurrentWidget(self.web_sheets)

        elif service_name == "slides":
            if not self.web_slides:
                self.web_slides = QWebEngineView()
                self.web_slides.load(QUrl("https://docs.google.com/presentation/u/0/"))
                self.stacked_widget.addWidget(self.web_slides)
            self.stacked_widget.setCurrentWidget(self.web_slides)

        elif service_name == "boosteroid":
            if not self.web_boosteroid:
                self.web_boosteroid = QWebEngineView()
                self.web_boosteroid.load(QUrl("https://boosteroid.com/"))
                self.stacked_widget.addWidget(self.web_boosteroid)
            self.stacked_widget.setCurrentWidget(self.web_boosteroid)

    def show_resources(self):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        mem_used_mb = mem.used / (1024 ** 2)

        msg = f"CPU usage: {cpu}%\nMemory used: {mem_used_mb:.2f} MB"
        QMessageBox.information(self, "System Resources", msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    shell = NimbusShell()
    shell.show()
    sys.exit(app.exec_())
