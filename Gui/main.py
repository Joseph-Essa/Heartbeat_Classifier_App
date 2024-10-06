import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
import requests
from image_processor import Ui_MainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.upload_button.clicked.connect(self.upload_image)

    def upload_image(self):

        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)")

        if file_name:

            self.process_image(file_name)

            pixmap = QPixmap(file_name)
            self.ui.imageLabel.setPixmap(pixmap)
            self.ui.imageLabel.setScaledContents(True) 

    def process_image(self, file_name):
        url = "http://127.0.0.1:8000/process-image/"
        with open(file_name, 'rb') as f:
            files = {'file': (file_name, f, 'image/png')}
            response = requests.post(url, files=files)

        if response.status_code == 200:
           self.ui.result_line_edit.setText("Success: " + response.json().get("message", "No message"))
        else:
           self.ui.result_line_edit.setText("Error: " + response.json().get("error", "Unknown error"))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())