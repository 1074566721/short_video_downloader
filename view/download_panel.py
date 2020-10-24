# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download_panel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 200)
        Form.setMinimumSize(QtCore.QSize(360, 200))
        Form.setMaximumSize(QtCore.QSize(360, 200))
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 281, 50))
        self.lineEdit.setStyleSheet("border-radius:8px;")
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.download_btn = QtWidgets.QPushButton(Form)
        self.download_btn.setGeometry(QtCore.QRect(40, 90, 110, 35))
        self.download_btn.setStyleSheet(".QPushButton,\n"
".QToolButton {\n"
"    background: #FFF;\n"
"    border: 1px solid #DCDFE6;\n"
"    color: #606266;\n"
"    padding: 5px;\n"
"    min-height: 15px;\n"
"    border-radius: 8px;\n"
"}\n"
".QPushButton:hover,\n"
".QToolButton:hover {\n"
"    color: #409EFF;\n"
"    border-color: #c6e2ff;\n"
"    background-color: #ecf5ff;\n"
"}\n"
"\n"
".QPushButton:pressed,\n"
".QToolButton:pressed {\n"
"    color: #3a8ee6;\n"
"    border-color: #3a8ee6;\n"
"    outline: 0;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon/douyin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_btn.setIcon(icon)
        self.download_btn.setIconSize(QtCore.QSize(26, 26))
        self.download_btn.setObjectName("download_btn")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 90, 110, 35))
        self.pushButton.setStyleSheet(".QPushButton,\n"
".QToolButton {\n"
"    background: #FFF;\n"
"    border: 1px solid #DCDFE6;\n"
"    color: #606266;\n"
"    padding: 5px;\n"
"    min-height: 15px;\n"
"    border-radius: 8px;\n"
"}\n"
".QPushButton:hover,\n"
".QToolButton:hover {\n"
"    color: #409EFF;\n"
"    border-color: #c6e2ff;\n"
"    background-color: #ecf5ff;\n"
"}\n"
"\n"
".QPushButton:pressed,\n"
".QToolButton:pressed {\n"
"    color: #3a8ee6;\n"
"    border-color: #3a8ee6;\n"
"    outline: 0;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icon/kuaishou.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 140, 110, 35))
        self.pushButton_2.setStyleSheet(".QPushButton,\n"
".QToolButton {\n"
"    background: #FFF;\n"
"    border: 1px solid #DCDFE6;\n"
"    color: #606266;\n"
"    padding: 5px;\n"
"    min-height: 15px;\n"
"    border-radius: 8px;\n"
"}\n"
".QPushButton:hover,\n"
".QToolButton:hover {\n"
"    color: #409EFF;\n"
"    border-color: #c6e2ff;\n"
"    background-color: #ecf5ff;\n"
"}\n"
"\n"
".QPushButton:pressed,\n"
".QToolButton:pressed {\n"
"    color: #3a8ee6;\n"
"    border-color: #3a8ee6;\n"
"    outline: 0;\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icon/pipigaoxiao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.download_btn_2 = QtWidgets.QPushButton(Form)
        self.download_btn_2.setGeometry(QtCore.QRect(40, 140, 110, 35))
        self.download_btn_2.setStyleSheet(".QPushButton,\n"
".QToolButton {\n"
"    background: #FFF;\n"
"    border: 1px solid #DCDFE6;\n"
"    color: #606266;\n"
"    padding: 5px;\n"
"    min-height: 15px;\n"
"    border-radius: 8px;\n"
"}\n"
".QPushButton:hover,\n"
".QToolButton:hover {\n"
"    color: #409EFF;\n"
"    border-color: #c6e2ff;\n"
"    background-color: #ecf5ff;\n"
"}\n"
"\n"
".QPushButton:pressed,\n"
".QToolButton:pressed {\n"
"    color: #3a8ee6;\n"
"    border-color: #3a8ee6;\n"
"    outline: 0;\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icon/weishi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_btn_2.setIcon(icon3)
        self.download_btn_2.setIconSize(QtCore.QSize(25, 25))
        self.download_btn_2.setObjectName("download_btn_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.download_kuaishou)
        self.download_btn.clicked.connect(Form.download_douyin)
        self.pushButton_2.clicked.connect(Form.download_pipigaoxiao)
        self.download_btn_2.clicked.connect(Form.download_weishi)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "短视频去水印下载器"))
        self.lineEdit.setPlaceholderText(_translate("Form", "请输入一条短视频分享链接"))
        self.download_btn.setText(_translate("Form", "抖音"))
        self.pushButton.setText(_translate("Form", "快手"))
        self.pushButton_2.setText(_translate("Form", "皮皮搞笑"))
        self.download_btn_2.setText(_translate("Form", "微视"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
