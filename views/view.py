# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Card(object):
    def setupUi(self, Card):
        Card.setObjectName("Card")
        Card.resize(266, 399)
        self.label = QtWidgets.QLabel(Card)
        self.label.setGeometry(QtCore.QRect(0, 0, 266, 399))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../database/pics/yuzuk.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Card)
        QtCore.QMetaObject.connectSlotsByName(Card)

    def retranslateUi(self, Card):
        _translate = QtCore.QCoreApplication.translate
        Card.setWindowTitle(_translate("Card", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Card = QtWidgets.QWidget()
    ui = Ui_Card()
    ui.setupUi(Card)
    Card.show()
    sys.exit(app.exec_())