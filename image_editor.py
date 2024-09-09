from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QPalette

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Image Editor")
main_window.resize(900, 700)

# ==== All app widgets/objects ====
btn_folder = QPushButton("Select Folder")
file_list = QListWidget()

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
mirror = QPushButton("Mirror")
sharpness = QPushButton("Sharpness")
gray = QPushButton("Gray")
saturation = QPushButton("Saturation")
contrast = QPushButton("Contrast")
blur = QPushButton("Blur")

# ========= Dropdown box =============
filter_box = QComboBox()
filter_box.addItem("Original")
filter_box.addItem("Left")
filter_box.addItem("Right")
filter_box.addItem("Mirror")
filter_box.addItem("Sharpness")
filter_box.addItem("Gray")
filter_box.addItem("Saturation")
filter_box.addItem("Contrast")
filter_box.addItem("Blur")

picture_box = QLabel("Image will appear here!")

#======= App Design ==============
master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

# col 1 
col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)

col1.addWidget(btn_left)
col1.addWidget(btn_right)
col1.addWidget(mirror)
col1.addWidget(sharpness)
col1.addWidget(gray)
col1.addWidget(saturation)
col1.addWidget(contrast)
col1.addWidget(blur)

# col 2 
col2.addWidget(picture_box)

# master layout 
master_layout.addLayout(col1,stretch=20)
master_layout.addLayout(col2,stretch=80)

# ==== Dark Mode Pallete =====
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
# ==============================

main_window.setLayout(master_layout)

main_window.show()
app.exec_()