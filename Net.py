# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Net.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import speedtest as st
import time


class Ui_NetS(object):
    def setupUi(self, NetS):
        NetS.setObjectName("NetS")
        NetS.resize(265, 281)
        self.label = QtWidgets.QLabel(NetS)
        self.label.setGeometry(QtCore.QRect(0, 0, 271, 51))

        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(NetS)
        self.pushButton.setGeometry(QtCore.QRect(80, 90, 111, 31))
        self.pushButton.setObjectName("pushButton")

        self.label_2 = QtWidgets.QLabel(NetS)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 171, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(NetS)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 181, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(NetS)
        self.label_4.setGeometry(QtCore.QRect(50, 225, 191, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(NetS)
        QtCore.QMetaObject.connectSlotsByName(NetS)

    def retranslateUi(self, NetS):
        _translate = QtCore.QCoreApplication.translate
        NetS.setWindowTitle(_translate("NetS", "NetS"))
        self.label.setText(_translate("NetS", "<html><head/><body><p><span style=\" color:#ffffff;\">NetS</span></p></body></html>"))

        self.pushButton.setText(_translate("NetS", "Get Net Speed"))
        self.pushButton.clicked.connect(self.get_net)

        self.label_2.setText(_translate("NetS", "Upload Speed"))
        self.label_3.setText(_translate("NetS", "Download Speed"))
        self.label_4.setText(_translate("NetS", "PING"))
        

    def get_net(self):
       
        self.label_2.setText("Calculating Upload Speed...")
        self.label_3.setText("Calculating Download Speed...")
        self.label_4.setText("Calculating PING...")

        QtWidgets.QApplication.processEvents()

        speed = st.Speedtest()

        ping = speed.results.ping
        download = speed.download()
        upload = speed.upload()

        ds = round(download / (10**6),2)
        us = round(upload / (10**6),2)

        self.label_2.setText("Upload Speed = " + str(us) + "Mbps")
        self.label_3.setText("Download Speed = " + str(ds) + "Mbps")
        self.label_4.setText("PING = " + str(ping) + "ms")

        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NetS = QtWidgets.QWidget()
    ui = Ui_NetS()
    ui.setupUi(NetS)
    NetS.show()
    sys.exit(app.exec_())
