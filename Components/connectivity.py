from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class ConnectivityPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        title = QLabel("Connectivity")
        



        raspberry_pi_box = QPushButton("Raspberry Pi")
        camera1_box = QPushButton("Camera1")
        camera2_box = QPushButton("Camera2")
        x_box_box = QPushButton("X box Controller")
        
        layout.addWidget(title)
        layout.addWidget(raspberry_pi_box)
        layout.addWidget(camera1_box)
        layout.addWidget(camera2_box)
        layout.addWidget(x_box_box)
        self.setLayout(layout)
