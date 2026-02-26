from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class HomePage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()

        title = QLabel("Chinese Practice App")
        vocab_btn = QPushButton("Vocabulario")
        dictation_btn = QPushButton("Dictado")

        vocab_btn.clicked.connect(lambda: self.main_window.navigate(1))
        dictation_btn.clicked.connect(lambda: self.main_window.navigate(2))

        layout.addWidget(title)
        layout.addWidget(vocab_btn)
        layout.addWidget(dictation_btn)

        self.setLayout(layout)
