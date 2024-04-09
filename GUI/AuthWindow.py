import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QRadioButton, QLabel, QDialogButtonBox

class AuthDialog(QDialog):
    def __init__(self, parent=None):
        super(AuthDialog, self).__init__(parent)
        self.setWindowTitle("Authentication Method")
        self.layout = QVBoxLayout(self)

        self.label = QLabel("Select Authentication Method:", self)
        self.layout.addWidget(self.label)

        self.passwordButton = QRadioButton("Password Authentication")
        self.keyButton = QRadioButton("Key Authentication")
        self.layout.addWidget(self.passwordButton)
        self.layout.addWidget(self.keyButton)

        self.passwordButton.setChecked(True)  # Default selection

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.layout.addWidget(self.buttonBox)
        self.passwd_auth = True
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def accept(self):
        if self.passwordButton.isChecked():
            self.passwd_auth = True
        elif self.keyButton.isChecked():
            self.passwd_auth = False
        super(AuthDialog, self).accept()



