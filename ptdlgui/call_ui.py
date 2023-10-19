import sys
from main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import requests
from PyQt5.QtGui import QImage, QPixmap
from ptdl.pytu import yt_gen, max_qldl, audio_ytdl
from pytube import YouTube


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
        # link and tittle generation
        self.yt = YouTube(self.ui.link_lineEdit.text(),
                          on_progress_callback=self.progress)
        self.vid_tittle = self.yt.title
        # lable setup
        self.vid_thumbnail = self.yt.thumbnail_url
        img_url = self.vid_thumbnail
        img = QImage()
        img.loadFromData(requests.get(img_url).content)
        self.ui.image_place.setPixmap(QPixmap(img))
        # enabling download after getting the link
        self.ui.download_pushButton.setEnabled(True)

    def videoDownload(self):
        self.ui.download_pushButton.setText("...")
        self.ui.progressBar.setValue(0)
        self.download_path = self.ui.path_lineEdit.text()
        self.ui.download_pushButton.setEnabled(False)
        if self.ui.max_radioButton.isChecked():
            max_qldl(self.yt, self.download_path, self.vid_tittle)
        if self.ui.audio_radioButton.isChecked():
            audio_ytdl(self.yt, self.download_path, self.vid_tittle)
        self.ui.download_pushButton.setEnabled(True)
        self.ui.progressBar.setValue(100)
        self.ui.download_pushButton.setText("Download")

    def progress(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        p = 0
        if p <= 99:
            p = (bytes_remaining/size)*100
            self.ui.progressBar.setValue(int(p))


def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    nowWindow = CallUI()
    nowWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    setUpWindow()
