import sys
from main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import requests
from PyQt5.QtGui import QImage, QPixmap
from ptdl.pytu import yt_gen, max_qldl
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
        self.yt = YouTube(self.ui.link_lineEdit.text(),
                          on_progress_callback=self.progress_func)
        self.vid_tittle = self.yt.title
        self.vid_thumbnail = self.yt.thumbnail_url
        img_url = self.vid_thumbnail
        img = QImage()
        img.loadFromData(requests.get(img_url).content)
        self.ui.image_place.setPixmap(QPixmap(img))
        self.ui.download_pushButton.setEnabled(True)

    def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

    def videoDownload(self):
        self.download_path = self.ui.path_lineEdit.text()
        self.ui.download_pushButton.setEnabled(False)
        max_qldl(self.yt, self.download_path, self.vid_tittle)
        self.ui.download_pushButton.setEnabled(True)

#    def progress_func(self, stream, chunk, bytes_remaining):
#        size = stream.filesize
#        p = 0
#        while p <= 100:
#            self.ui.progressBar.setValue(int(p))
#            p = self.percent(bytes_remaining, size)


def setUpWindow():
    app = QtWidgets.QApplication(sys.argv)
    nowWindow = CallUI()
    nowWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    setUpWindow()
