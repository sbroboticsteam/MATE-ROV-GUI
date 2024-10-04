from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QGroupBox

class ConnectivityPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        main_groupbox = QGroupBox()

        #Grouping the 4 buttons together
        groupbox = QGroupBox()
        groupbox_layout = QVBoxLayout()
        title = QLabel("Connectivity")
        title.setStyleSheet("background-color: #555555; color: white; padding: 2.5px")
        title.setFixedHeight(25)

        raspberry_pi_box = QPushButton("Raspberry Pi")
        raspberry_pi_box.setStyleSheet("background-color: #297A14; color: white; padding: 10px; border-radius: 15px")
        camera1_box = QPushButton("Camera1")
        camera1_box.setStyleSheet("background-color: #9A3413; color: white; padding: 10px; border-radius: 15px ")
        camera2_box = QPushButton("Camera2")
        camera2_box.setStyleSheet("background-color: #9A3413; color: white; padding: 10px; border-radius: 15px")
        x_box_box = QPushButton("X box Controller")
        x_box_box.setStyleSheet("background-color: #297A14; color: white; padding: 10px; border-radius: 15px")
        

        layout.addWidget(title)
        groupbox_layout.addWidget(raspberry_pi_box)
        groupbox_layout.addWidget(camera1_box)
        groupbox_layout.addWidget(camera2_box)
        groupbox_layout.addWidget(x_box_box)
        groupbox.setLayout(groupbox_layout)
        layout.addWidget(groupbox)
        main_groupbox.setLayout(layout)
        self.setLayout(layout)
