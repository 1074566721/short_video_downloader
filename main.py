from PyQt5.Qt import *

from model.thread_api import GetDouyinThread, GetPipigaoxiaoThread, GetKuaishouThread, GetWeishiThread
from view.download_panel import Ui_Form
import view.icon_rc

url_text = ''


class Download_panel(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)


    def download_weishi(self):
        global url_text
        url_text = self.lineEdit.text()
        thread = GetWeishiThread(self, url_text)  # 开启一个子线程用于下载视频
        self.create_thread(thread)  # 创建一个子线程

    def download_pipigaoxiao(self):
        global url_text
        url_text = self.lineEdit.text()
        thread = GetPipigaoxiaoThread(self, url_text)  # 开启一个子线程用于下载视频
        self.create_thread(thread)  # 创建一个子线程

    def download_douyin(self):
        # print('点击了下载')
        self.download_btn.setEnabled(False)  # 如果点击了下载则设置按钮为不可用
        global url_text
        url_text = self.lineEdit.text()
        thread = GetDouyinThread(self, url_text)  # 开启一个子线程用于下载视频
        self.create_thread(thread)  # 创建一个子线程

    def download_kuaishou(self):
        # print('点击了下载')
        self.download_btn.setEnabled(False)  # 如果点击了下载则设置按钮为不可用
        global url_text
        url_text = self.lineEdit.text()
        thread = GetKuaishouThread(self, url_text)  # 开启一个子线程用于下载视频
        self.create_thread(thread)  # 创建一个子线程

    def set_progess_value(self, value):
        self.progress.setValue(value)
        if value == 100:  # 当视频下载完成后，弹出提示窗口
            QMessageBox.information(self, "提示", "下载成功！")
            self.download_btn.setEnabled(True)
            return

    def fail_tips(self):
        # 当视频下载失败后，弹出提示窗口
        QMessageBox.warning(self, '警告', '链接解析错误！\n请检查链接后重新输入~')
        self.download_btn.setEnabled(True)

    def create_thread(self, thread):
        thread.fail_download_signal.connect(self.fail_tips)
        thread.proess_value_signal.connect(self.set_progess_value)
        thread.start_download_signal.connect(lambda: self.progress.setLabelText('解析完成，下载中……'))
        thread.finish_compile_signal.connect(lambda: self.create_progessdialog())  # 实例化一个进度条提示框
        thread.start()

    def create_progessdialog(self):
        self.progress = QProgressDialog('链接解析中……', '取消', 0, 100, self, Qt.WindowCloseButtonHint)
        self.progress.setWindowTitle('开始下载')
        self.progress.setCancelButton(None)
        self.progress.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Download_panel()
    window.show()
    sys.exit(app.exec_())
