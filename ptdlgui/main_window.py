# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Youtube_downloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lable_Video_link = QtWidgets.QLabel(self.centralwidget)
        self.lable_Video_link.setObjectName("lable_Video_link")
        self.gridLayout.addWidget(self.lable_Video_link, 0, 0, 1, 1)
        self.link_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.link_lineEdit.setObjectName("link_lineEdit")
        self.gridLayout.addWidget(self.link_lineEdit, 1, 0, 1, 1)
        self.enter_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.enter_pushButton.setObjectName("enter_pushButton")
        self.gridLayout.addWidget(self.enter_pushButton, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.image_place = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_place.sizePolicy().hasHeightForWidth())
        self.image_place.setSizePolicy(sizePolicy)
        self.image_place.setMinimumSize(QtCore.QSize(0, 250))
        self.image_place.setText("")
        self.image_place.setScaledContents(True)
        self.image_place.setObjectName("image_place")
        self.verticalLayout_2.addWidget(self.image_place)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.quality_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.quality_comboBox.setObjectName("quality_comboBox")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.gridLayout_2.addWidget(self.quality_comboBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.max_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.max_radioButton.setCheckable(True)
        self.max_radioButton.setChecked(False)
        self.max_radioButton.setAutoRepeatDelay(300)
        self.max_radioButton.setObjectName("max_radioButton")
        self.verticalLayout.addWidget(self.max_radioButton)
        self.audio_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.audio_radioButton.setObjectName("audio_radioButton")
        self.verticalLayout.addWidget(self.audio_radioButton)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 2, 2, 1)
        self.quality_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.quality_horizontalSlider.setMinimum(0)
        self.quality_horizontalSlider.setMaximum(5)
        self.quality_horizontalSlider.setProperty("value", 4)
        self.quality_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.quality_horizontalSlider.setObjectName("quality_horizontalSlider")
        self.gridLayout_2.addWidget(self.quality_horizontalSlider, 2, 0, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.path_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.path_lineEdit.setMinimumSize(QtCore.QSize(295, 0))
        self.path_lineEdit.setObjectName("path_lineEdit")
        self.gridLayout_4.addWidget(self.path_lineEdit, 1, 0, 1, 1)
        self.edit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.edit_pushButton.setMaximumSize(QtCore.QSize(84, 36))
        self.edit_pushButton.setObjectName("edit_pushButton")
        self.gridLayout_4.addWidget(self.edit_pushButton, 1, 1, 1, 1)
        self.download_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.download_pushButton.setEnabled(False)
        self.download_pushButton.setMaximumSize(QtCore.QSize(84, 36))
        self.download_pushButton.setObjectName("download_pushButton")
        self.gridLayout_4.addWidget(self.download_pushButton, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.quality_comboBox.setCurrentIndex(4)
        self.quality_horizontalSlider.sliderMoved['int'].connect(self.quality_comboBox.setCurrentIndex) # type: ignore
        self.quality_comboBox.currentIndexChanged['int'].connect(self.quality_horizontalSlider.setValue) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloader"))
        self.lable_Video_link.setText(_translate("MainWindow", "Video Link"))
        self.link_lineEdit.setText(_translate("MainWindow", "https://www.youtube.com"))
        self.enter_pushButton.setText(_translate("MainWindow", "Enter"))
        self.quality_comboBox.setItemText(0, _translate("MainWindow", "144p"))
        self.quality_comboBox.setItemText(1, _translate("MainWindow", "240p"))
        self.quality_comboBox.setItemText(2, _translate("MainWindow", "360p"))
        self.quality_comboBox.setItemText(3, _translate("MainWindow", "480p"))
        self.quality_comboBox.setItemText(4, _translate("MainWindow", "720p"))
        self.quality_comboBox.setItemText(5, _translate("MainWindow", "1080p"))
        self.label_2.setText(_translate("MainWindow", "Video Quality"))
        self.max_radioButton.setText(_translate("MainWindow", "Max Quality"))
        self.max_radioButton.setShortcut(_translate("MainWindow", "Q"))
        self.audio_radioButton.setText(_translate("MainWindow", "Audio Only"))
        self.audio_radioButton.setShortcut(_translate("MainWindow", "A"))
        self.label.setText(_translate("MainWindow", "Download Path"))
        self.edit_pushButton.setText(_translate("MainWindow", "Edit"))
        self.download_pushButton.setText(_translate("MainWindow", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())