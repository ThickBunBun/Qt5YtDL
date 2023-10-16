import sys
from main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import requests
from PyQt5.QtGui import QImage, QPixmap
from ptdl.pytu import yt_gen, max_qldl


class CallUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setUpEnterButton()
        self.setUpDownloadButton()

    def setUpEnterButton(self):
        self.ui.enter_pushButton.clicked.connect(self.infoSet)

    def setUpDownloadButton(self):
        self.ui.download_pushButton.clicked.connect(self.videoDownload)

    def infoSet(self):
        self.yt, self.vid_tittle, self.vid_thumbnail = yt_gen(
            self.ui.link_lineEdit.text())
        img_url = self.vid_thumbnail
        img = QImage()
        img.loadFromData(requests.get(img_url).content)
        self.ui.image_place.setPixmap(QPixmap(img))

    def videoDownload(self):
        self.download_path = self.ui.path_lineEdit.text()
        max_qldl(self.yt, self.download_path, self.vid_tittle)


def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    nowWindow = CallUI()
    nowWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    setUpWindow()
