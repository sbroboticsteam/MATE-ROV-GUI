from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class ConnectivityPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        button1 = QPushButton("Testing")
        button2 = QPushButton()
        button3 = QPushButton()
        
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        self.setLayout(layout)
