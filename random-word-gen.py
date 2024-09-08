from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QLabel , QPushButton, QVBoxLayout , QHBoxLayout
import random

RANDOM_WORDS = ["Hello","goodbye","test","app","python","pyqt","India","asia"]
def random_word(text):
    word = random.choice(RANDOM_WORDS)
    if text == 1:
        text1.setText(word)
    elif text == 2:
        text2.setText(word)
    elif text == 3:
        text3.setText(word)
    elif text == 0:
        text1.setText("?")
        text2.setText("?")
        text3.setText("?")

#App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Word maker")
main_window.resize(300, 200)

#creating all app objects
title = QLabel("<h1>Random Word Generator</h1>")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")
button4 = QPushButton("Reset")

#all design here

master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()

row1.addWidget(title,alignment=Qt.AlignCenter)

row2.addWidget(text1,alignment=Qt.AlignCenter)
row2.addWidget(text2,alignment=Qt.AlignCenter)
row2.addWidget(text3,alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

row4.addWidget(button4,stretch=2,alignment=Qt.AlignCenter)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)
master_layout.addLayout(row4)

main_window.setLayout(master_layout)

#Event Handling

button1.clicked.connect(lambda : random_word(1))
button2.clicked.connect(lambda : random_word(2))
button3.clicked.connect(lambda : random_word(3))
button4.clicked.connect(lambda : random_word(0))

#Create all objects/widgets below here

# print(x for x in range(10))

main_window.show()
app.exec()