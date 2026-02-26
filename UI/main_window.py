from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QStackedWidget,
)

from UI.pages.home_page import HomePage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chinese Trainer")
        self.setMinimumSize(800, 500)

        self._init_ui()

    def _init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout()
        central.setLayout(layout)

        # Stack de páginas
        self.stack = QStackedWidget()

        self.home_page = HomePage(self)
        # self.vocab_page = VocabPage(self)
        # self.dictation_page = DictationPage(self)

        self.stack.addWidget(self.home_page)
        # self.stack.addWidget(self.vocab_page)
        # self.stack.addWidget(self.dictation_page)

        layout.addWidget(self.stack)

    def navigate(self, index: int):
        self.stack.setCurrentIndex(index)
