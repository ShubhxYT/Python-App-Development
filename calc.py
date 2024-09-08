from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QLabel , QPushButton, QVBoxLayout , QHBoxLayout ,QLineEdit ,QGridLayout
from PyQt5.QtGui import QFont

class CalcApp(QWidget):
    #settings
    def __init__(self):
        super().__init__()
        #App Settings
        self.setWindowTitle("Calculator in pyqt")
        self.resize(300, 400)

        #all objects/widgets
        self.text_box = QLineEdit()
        # self.text_box.setFont(QFont("Helvetica",32, QFont.Bold))
        self.text_box.setStyleSheet("QLineEdit {color: black; background-color: white; font: 36pt Helvetica;}")
        
        
        self.grid = QGridLayout()

        self.buttons = [
            "7",'8','9',"/",
            '4','5','6',"*",
            '1','2','3',"-",
            '0',".","=","+"
            ]

        row , col = 0,0
        for text in self.buttons:
            button = QPushButton(text)
            # write_text(text)     
            button.clicked.connect(self.write_text)
            
            button.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding:10px;background-color:grey;}")#,"background-color:grey"
            self.grid.addWidget(button,row,col)

            col+=1
            if col > 3:
                row+=1
                col=0

        self.clear = QPushButton("Clear")
        self.delete = QPushButton("<-")
        self.clear.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding:10px;background-color:grey;}")#,"background-color:grey"
        self.delete.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding:10px;background-color:grey;}")
        
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25,25,25,25)
        
        self.setLayout(master_layout)
        
        self.clear.clicked.connect(self.write_text)
        self.delete.clicked.connect(self.write_text)
        
    def write_text(self):
        button = app.sender()
        text = button.text()
        
        text_on_box = self.text_box.text()
        if text_on_box == "Error":
            self.text_box.setText("")
            text_on_box = ""
            
        if text == "=":
            try:
                ans = eval(text_on_box)
                self.text_box.setText(str(ans))
            except:
                self.text_box.setText("Error")
                
        elif text == "Clear":
            self.text_box.setText("")
        elif text == "<-":
            self.text_box.setText(text_on_box[:-1])
        else:
            self.text_box.setText(text_on_box + text)
        # print(text)

    
    

#show/run
if __name__ == "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget {background-color: #f0f0f8;background-color:black;}")
    
    main_window.show()
    app.exec_()