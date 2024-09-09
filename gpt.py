from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QPalette

class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Editor")
        self.resize(900, 700)

        # Initialize UI components
        self.initUI()

    def initUI(self):
        # Dark mode toggle button
        self.dark_mode_button = QPushButton("Toggle Dark Mode")
        self.dark_mode_button.clicked.connect(self.toggle_dark_mode)

        # App widgets/objects
        self.btn_folder = QPushButton("Select Folder")
        self.file_list = QListWidget()

        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")
        self.mirror = QPushButton("Mirror")
        self.sharpness = QPushButton("Sharpness")
        self.gray = QPushButton("Gray")
        self.saturation = QPushButton("Saturation")
        self.contrast = QPushButton("Contrast")
        self.blur = QPushButton("Blur")

        # Dropdown box
        self.filter_box = QComboBox()
        self.filter_box.addItem("Original")
        self.filter_box.addItem("Left")
        self.filter_box.addItem("Right")
        self.filter_box.addItem("Mirror")
        self.filter_box.addItem("Sharpness")
        self.filter_box.addItem("Gray")
        self.filter_box.addItem("Saturation")
        self.filter_box.addItem("Contrast")
        self.filter_box.addItem("Blur")

        self.picture_box = QLabel("Image will appear here!")

        # App Design
        master_layout = QHBoxLayout()

        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        # Column 1
        col1.addWidget(self.btn_folder)
        col1.addWidget(self.file_list)
        col1.addWidget(self.filter_box)

        col1.addWidget(self.btn_left)
        col1.addWidget(self.btn_right)
        col1.addWidget(self.mirror)
        col1.addWidget(self.sharpness)
        col1.addWidget(self.gray)
        col1.addWidget(self.saturation)
        col1.addWidget(self.contrast)
        col1.addWidget(self.blur)

        # Column 2
        col2.addWidget(self.dark_mode_button, alignment=Qt.AlignRight)  # Add dark mode button
        col2.addWidget(self.picture_box)

        # Master layout
        master_layout.addLayout(col1, stretch=20)
        master_layout.addLayout(col2, stretch=80)

        self.setLayout(master_layout)

        # Initial theme
        self.is_dark_mode = True
        self.apply_theme()

    def toggle_dark_mode(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.is_dark_mode:
            dark_palette = QPalette()
            dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.WindowText, Qt.white)
            dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
            dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
            dark_palette.setColor(QPalette.ToolTipText, Qt.white)
            dark_palette.setColor(QPalette.Text, Qt.white)
            dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ButtonText, Qt.white)
            dark_palette.setColor(QPalette.Highlight, QColor(142, 45, 197))
            dark_palette.setColor(QPalette.HighlightedText, Qt.white)

            QApplication.setPalette(dark_palette)
        else:
            light_palette = QPalette()
            light_palette.setColor(QPalette.Window, Qt.white)
            light_palette.setColor(QPalette.WindowText, Qt.black)
            light_palette.setColor(QPalette.Base, Qt.white)
            light_palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
            light_palette.setColor(QPalette.ToolTipBase, Qt.black)
            light_palette.setColor(QPalette.ToolTipText, Qt.white)
            light_palette.setColor(QPalette.Text, Qt.black)
            light_palette.setColor(QPalette.Button, Qt.white)
            light_palette.setColor(QPalette.ButtonText, Qt.black)
            light_palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
            light_palette.setColor(QPalette.HighlightedText, Qt.white)

            QApplication.setPalette(light_palette)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.show()
    sys.exit(app.exec_())
