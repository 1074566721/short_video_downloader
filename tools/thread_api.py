from PyQt5.Qt import *

from tools import get_video


class GetVideoThread(QThread):
    fail_download_signal = pyqtSignal()
    proess_value_signal = pyqtSignal(int)
    start_download_signal = pyqtSignal()
    finish_compile_signal = pyqtSignal()

    def __init__(self, parent=None, class_name=None, url_text=None):
        super(GetVideoThread, self).__init__(parent=parent)
        self.class_name = class_name
        self.url_text = url_text

    def request_url(self, first_url, video_name):
        pass

    def run(self) -> None:
        global url_text
        first_url, video_name = self.class_name.compile_name_url(self.url_text)
        print('视频名：{}，链接：{}'.format(video_name, first_url))
        if first_url is None or video_name is None:  # 判断解析出来的文件名和链接是否正确，不正确则直接结束线程
            self.fail_download_signal.emit()
            return
        # 如果正确，就返回完成解析的信号，给主窗口调出进度条
        self.finish_compile_signal.emit()
        self.request_url(first_url, video_name)

    def save_video(self, video_name, video):
        file_size = video.headers['Content-Length']  # 获取文件的大小值
        buffer = 128  # 每次下载的大小
        offset = 0  # 偏移值
        with open(video_name + ".mp4", 'wb')as file:
            for chunk in video.iter_content(chunk_size=buffer):
                if not chunk: break
                file.seek(offset)
                file.write(chunk)
                offset = offset + len(chunk)
                progess_value = offset / int(file_size) * 100
                self.proess_value_signal.emit(progess_value)

            print("===>视频下载完成！")
class GetWeishiThread(GetVideoThread):
    def __init__(self, parent=None, url_text=None):
        super(GetWeishiThread, self).__init__(parent=parent, class_name=get_video.GetWeishiVideo,
                                                   url_text=url_text)

    def request_url(self, feedid, video_name):
        while True:
            video_url=get_video.GetWeishiVideo.first_request(feedid)
            flag,video =get_video.GetWeishiVideo.second_requset(video_url)
            print('返回的标记:{}和视频:{}'.format(flag, video))
            if 200 == flag:
                self.start_download_signal.emit()  # 发射开始下载的信号
                self.save_video(video_name, video)
                return
            print('{:-^50}'.format('请求失败，重新请求！'))

class GetPipigaoxiaoThread(GetVideoThread):
    def __init__(self, parent=None, url_text=None):
        super(GetPipigaoxiaoThread, self).__init__(parent=parent, class_name=get_video.GetPipigaoxiaoVideo,
                                                   url_text=url_text)

    def request_url(self, first_url, video_name):
        while True:
            flag, video = get_video.GetPipigaoxiaoVideo.first_request(first_url)
            print('返回的标记:{}和视频:{}'.format(flag, video))
            if 200 == flag:
                self.start_download_signal.emit()  # 发射开始下载的信号
                self.save_video(video_name, video)
                return
            print('{:-^50}'.format('请求失败，重新请求！'))


class GetDouyinThread(GetVideoThread):
    def __init__(self, parent=None, url_text=None):
        super(GetDouyinThread, self).__init__(parent=parent, class_name=get_video.GetDouyinVideo, url_text=url_text)

    def request_url(self, first_url, video_name):
        params = get_video.GetDouyinVideo.first_request(first_url)
        play_url = get_video.GetDouyinVideo.second_request(params)
        while True:
            video_url = get_video.GetDouyinVideo.third_request(play_url)
            flag, video = get_video.GetDouyinVideo.fourth_request(video_url)
            print('返回的标记:{}和视频:{}'.format(flag, video))
            if 403 != flag:
                self.start_download_signal.emit()  # 发射开始下载的信号
                self.save_video(video_name, video)
                return
            print('{:-^50}'.format('请求失败，重新请求！'))


class GetKuaishouThread(GetVideoThread):
    def __init__(self, parent=None, url_text=None):
        super(GetKuaishouThread, self).__init__(parent=parent, class_name=get_video.GetKuaishouVideo, url_text=url_text)

    def request_url(self, first_url, video_name):
        second_url = get_video.GetKuaishouVideo.first_request(first_url)
        while True:
            video_url = get_video.GetKuaishouVideo.second_request(second_url)
            flag, video = get_video.GetKuaishouVideo.third_request(video_url)
            print('返回的标记:{}和视频:{}'.format(flag, video))
            if 200 == flag:
                self.start_download_signal.emit()  # 发射开始下载的信号
                self.save_video(video_name, video)
                return
            print('{:-^50}'.format('请求失败，重新请求！'))
