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
        self.title = QLabel('Git Operations UI', self)
        layout.addWidget(self.title)

        # Input field for commit message
        self.commit_msg_input = QLineEdit(self)
        self.commit_msg_input.setPlaceholderText("Enter commit message")
        layout.addWidget(self.commit_msg_input)

        # Output field for logging Git commands output
        self.output_field = QTextEdit(self)
        self.output_field.setReadOnly(True)
        layout.addWidget(self.output_field)

        # Buttons for git operations
        self.add_button = QPushButton('Add Files', self)
        self.add_button.clicked.connect(self.git_add)
        layout.addWidget(self.add_button)

        self.commit_button = QPushButton('Commit Changes', self)
        self.commit_button.clicked.connect(self.git_commit)
        layout.addWidget(self.commit_button)

        self.push_button = QPushButton('Push to GitHub', self)
        self.push_button.clicked.connect(self.git_push)
        layout.addWidget(self.push_button)

        # Set layout
        self.setLayout(layout)
        self.setWindowTitle('Git UI')
        self.show()

    def run_git_command(self, command):
        """Helper method to run Git commands and capture output"""
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            self.output_field.append(result.decode())
        except subprocess.CalledProcessError as e:
            self.output_field.append(f"Error: {e.output.decode()}")

    def git_add(self):
        """Add all files to staging"""
        self.output_field.append("Running git add ...")
        self.run_git_command("git add .")

    def git_commit(self):
        """Commit changes with user input"""
        commit_msg = self.commit_msg_input.text()
        if not commit_msg:
            self.output_field.append("Commit message cannot be empty!")
            return
        self.output_field.append(f"Committing changes with message: {commit_msg}")
        self.run_git_command(f"git commit -m \"{commit_msg}\"")

    def git_push(self):
        """Push to remote GitHub repo"""
        self.output_field.append("Pushing changes to GitHub...")
        self.run_git_command("git push origin main")

# if __name__ == '__main__':
app = QApplication(sys.argv)
ex = GitUI()
sys.exit(app.exec_())
