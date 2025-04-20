import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTextEdit

class GitUI(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the UI
        self.init_ui()

    def init_ui(self):
        # Layout
        layout = QVBoxLayout()

        # Title label
        self.title = QLabel('Mallu Jarvis', self)
        layout.addWidget(self.title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GitUI()
    sys.exit(app.exec_())
