import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QPalette , QPixmap
from PIL import Image, ImageEnhance, ImageFilter

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

picture_box = QLabel("Image will appear here!",alignment=Qt.AlignCenter)

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


# All App Functionality

working_directory = ""
# working_directory = "/home/somani/Documents/codes/Python App Development/Images"

# Filter files and extensions

def filter(files,extensions):
    filter_files = []
    for file in files:
        for extension in extensions:
            if file.endswith(extension):
                filter_files.append(file)
    return filter_files

# Choose current work directory

def getWorkDirectory():
    global working_directory
    working_directory = QFileDialog.getExistingDirectory(main_window, "Select Directory")
    extentions = [".png",".jpg",".jpeg"]
    file_names = filter(os.listdir(working_directory),extentions)
    file_list.clear()
    for file in file_names:
        file_list.addItem(file)

# ======= All Editor Functions ===========    
class Editor():
    def __init__(self):
        self.image = None
        self.original = None
        self.filename = None
        self.save_folder = "edits/"
        
        self.editor_functions = {
                "Left": lambda image : image.transpose(Image.ROTATE_90),
                "Right": lambda image : image.transpose(Image.ROTATE_270),
                "Mirror": lambda image : image.transpose(Image.FLIP_LEFT_RIGHT),
                "Sharpness": lambda image : image.filter(ImageFilter.SHARPEN),
                "Gray": lambda image : image.convert("L"),
                "Saturation": lambda image : ImageEnhance.Color(image).enhance(1.2),
                "Contrast": lambda image : ImageEnhance.Contrast(image).enhance(1.2),
                "Blur": lambda image : image.filter(ImageFilter.BLUR)
            }
        
    def load_image(self,filename):
        self.filename = filename
        fullname = os.path.join(working_directory,self.filename)
        self.image = Image.open(fullname)
        self.original = self.image.copy()
        
    def save_image(self):
        path = os.path.join(working_directory,self.save_folder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        
        fullname = os.path.join(path,self.filename)
        self.image.save(fullname)
        
    def show_image(self,path):
        picture_box.hide()
        image = QPixmap(path)
        w , h = picture_box.width(), picture_box.height()
        image = image.scaled(w,h,Qt.KeepAspectRatio)
        picture_box.setPixmap(image)
        picture_box.show()
       
    def transformImage(self,transformation):
        transformations = self.editor_functions
        transform_function = transformations.get(transformation)
        
        if transform_function:
            self.image = transform_function(self.image)
            self.save_image()
            
        self.save_image()
        image_path = os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)
        
    def apply_filter(self,filter_name):
        if filter_name == "Original":
            self.image = self.original.copy()
            
        else:
            filter_function = self.editor_functions.get(filter_name)
            if filter_function:
                self.image = filter_function(self.image)
                self.save_image()
                image_path = os.path.join(working_directory,self.save_folder,self.filename)
                self.show_image(image_path)
        
        self.save_image()
        image_path = os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)

def handle_filter():
    if file_list.currentRow() >= 0 :
        select_filter = filter_box.currentText()
        editor.apply_filter(select_filter)

def displayImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        editor.load_image(filename)
        editor.show_image(os.path.join(working_directory,filename))
        # editor.save_folder = filename
        # filter_box.setCurrentIndex(0)
        
editor = Editor()
btn_folder.clicked.connect(getWorkDirectory)
file_list.currentRowChanged.connect(displayImage)
filter_box.currentTextChanged.connect(handle_filter)

btn_left.clicked.connect(lambda: editor.transformImage("Left"))
btn_right.clicked.connect(lambda: editor.transformImage("Right"))
mirror.clicked.connect(lambda: editor.transformImage("Mirror"))
sharpness.clicked.connect(lambda: editor.transformImage("Sharpness"))
gray.clicked.connect(lambda: editor.transformImage("Gray"))
contrast.clicked.connect(lambda: editor.transformImage("Contrast"))
blur.clicked.connect(lambda: editor.transformImage("Blur"))

main_window.show()
app.exec_()