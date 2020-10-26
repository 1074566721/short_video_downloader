import requests, re


class GetDouyinVideo():

    @staticmethod
    def compile_name_url(url_text):
        '''
        用正则匹配用户分享的抖音短视频链接，分别解析出空白符前的字符作为文件名，网页链接作为第一次请求所用的链接
        :param url_text: 用户输入的视频分享链接文本
        :return: 成功返回解析出的视频文件名和视频链接
                 失败返回两个None
        '''
        # 正则匹配分享链接，获取链接非空字符前的几个字符作为文件名
        video_name = re.match(r'\S*', url_text)
        if video_name:
            video_name = video_name.group()
            print(video_name)

        # 正则匹配分享链接，获取链接
        first_url = re.search(r'https://v.douyin.com/.*?/', url_text)
        if first_url:
            first_url = first_url.group()
            print('第一次url==》', first_url)

        return first_url, video_name

    @staticmethod
    def first_request(first_url):
        '''
        第一次发起请求，获取第二次请求需要的参数
        :param first_url: 第一次请求需要的url地址
        :return: 第二请求需要的参数
        '''
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'sec-fetch-dest': 'document',
            'sec-fetch-moe': 'navigate',
            'sec-fetch-site': 'none',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4195.1 Mobile Safari/537.36'
        }

        response = requests.get(first_url, headers=headers)

        print('第二次url==》', response.url)  # 获取第一次重定向后的url

        # 截取第二次请求需要的参数
        content = re.search(r'\d\d*\d', response.url).group()
        params = {"item_ids": content}

        return params

    @staticmethod
    def second_request(params):
        '''
        发起第二次请求，获取到json，在json中获取下一次请求需要的url链接
        :param params: 请求需要的参数值
        :return: 去水印后的url链接
        '''
        response = requests.get('https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/', params=params)
        result = response.json()  # 获得第二次请求的json，并从json中查找第三次请求需要的url
        # print(result)
        second_url = result['item_list'][0]['video']['play_addr']['url_list'][0]

        play_url = re.sub(r'playwm', 'play', second_url)
        print('第三次url==》', play_url)
        return play_url

    @staticmethod
    def third_request(play_url):
        '''
        发起第三次请求，获取第四个请求需要的url地址
        :param play_url: 本次请求需要的url
        :return: 下次请求需要的url
        '''
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4195.1 Mobile Safari/537.36'
        }
        # 执行第三次请求，获取定三次重定向的url
        response = requests.get(play_url, headers=headers)
        video_url = response.url
        print('第四次url==》', video_url)
        return video_url

    @staticmethod
    def fourth_request(video_url):
        '''
        第四次请求，最后一次请求，获取最终视频的下载链接
        :param third_url: 本次请求需要的url
        :return: flag用于判断请求是否成功的标记，video请求获取的内容（二进制）
        '''
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'identity;q=1, *;q=0',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'v3-dy-b.ixigua.com',
            'Range': 'bytes=0-',
            'Referer': video_url,
            'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4195.1 Mobile Safari/537.36'
        }

        video = requests.get(video_url, headers=headers)  # 最终视频所在的链接

        print('第五次url==》', video)
        flag = video.status_code
        # print(flag,type(flag))
        return flag, video

    # @staticmethod
    # def save_video(video_name, video_content):
    #     '''
    #     保存请求到的二进制编码
    #     :param video_name: 视频名
    #     :param video_content: 视频的url
    #     '''
    #     # print(video.content)
    #     with open(video_name + ".mp4", 'wb')as file:
    #         file.write(video_content.content)
    #         print("===>视频下载完成！")


class GetKuaishouVideo():
    @staticmethod
    def compile_name_url(url_text):
        video_name = re.match(r'\S*', url_text)
        if video_name:
            video_name = video_name.group()
            print(video_name)

        # 正则匹配分享链接，获取链接
        first_url = re.search(r'https://v.kuaishou.com/.*\s', url_text)
        if first_url:
            first_url = first_url.group()
            print('第一次url==》', first_url)

        return first_url, video_name

    @staticmethod
    def first_request(first_url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'v.kuaishou.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4195.1 Mobile Safari/537.36'
        }

        response = requests.get(first_url, headers=headers)
        second_url = response.url  # 获取重定向后的url地址
        print(second_url)
        return second_url

    @staticmethod
    def second_request(second_url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'did=web_209e6a4e64064f659be838aca3178ec1; didv=1603355622000',
            'Host': 'c.kuaishou.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4195.1 Mobile Safari/537.36'
        }
        response = requests.get(second_url, headers=headers)

        # https://txmov2.a.yximgs.com/bs2/newWatermark/Mzc5NDg4OTkxNjU_zh_4.mp4
        content = response.text
        print(content)
        # "srcNoMark":"https://txmov2.a.yximgs.com/upic/2020/10/19/21/BMjAyMDEwMTkyMTQ1MDRfMTg1NjY1NDIyMV8zNzk0ODg5OTE2NV8xXzM=_b_B00dec48f91be3a545f2e7d0dea127acc.mp4?clientCacheKey=3x84ejxivx6vgeu_b.mp4&tt=b&di=716808c2&bp=13380"}
        video_url = re.search(r'"srcNoMark":"https://txmov2.a.yximgs.com/.*?\"', content).group()[13:-1]
        print(video_url)

        return video_url

    @staticmethod
    def third_request(video_url):
        video = requests.get(video_url)
        flag = video.status_code
        return flag, video


class GetPipigaoxiaoVideo():  # 皮皮搞笑
    @staticmethod
    def compile_name_url(url_text):
        if url_text == '':
            return None, None
        headers = {
            'Host': 'share.ippzone.com',
            'Origin': 'http://share.ippzone.com',
            'Referer': url_text,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
        }
        mid = re.findall(r'mid=(\d*)', url_text)
        pid = re.findall(r'pid=(\d*)', url_text)
        if mid and pid:
            mid = int(mid[0])
            pid = int(pid[0])
        else:
            return None, None
        print(mid, pid)

        parmer = {
            'mid': mid,
            'pid': pid,
            'type': 'post'
        }
        url = 'http://share.ippzone.com/ppapi/share/fetch_content'
        r = requests.post(url, headers=headers, json=parmer)
        # print(r.content)
        result=r.json()
        print(result)

        video_name = result['data']['post']['content'].replace(' ', '')
        video_url = result['data']['post']['videos'][str(result['data']['post']['imgs'][0]['id'])]['url']
        return video_url, video_name

    @staticmethod
    def first_request(video_url):
        video = requests.get(video_url)
        flag = video.status_code
        print(flag)
        return flag, video
        # with open(str(video_name) + '.mp4', 'wb') as f:
        #     f.write(video)
        # print("【皮皮搞笑】: {}.mp4 无水印视频下载完成！".format(video_name))


class GetWeishiVideo():
    @staticmethod
    def compile_name_url(url_text):
        video_name = re.findall(r'(\w*)', url_text)
        feedid = re.findall(r'feed/(\w*)', url_text)
        if video_name and feedid:
            video_name = video_name[0]
            feedid = feedid[0]
        else:
            return None, None
        print(video_name, feedid)

        return feedid, video_name

    @staticmethod
    def first_request(feedid):
        headers = {
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-length': '84',
            'content-type': 'application/json',
            'cookie': 'RK=BuAQ1v+yV3; ptcz=6f7072f84fa03d56ea047b407853df6a5375d719df1031ef066d11b09fb679e4; pgv_pvi=8434466816; pgv_pvid=1643353500; tvfe_boss_uuid=3b10306bf3ae662b; o_cookie=1074566721; pac_uid=1_1074566721; ied_qq=o1074566721; LW_sid=k1Y5n9s3Y0K866h7P246v4k6o8; LW_uid=u1v5i9V3p0L806m7R226s4W7F1; eas_sid=J1p5G9s3A0h8Z6c7l2a6x4E7w7; iip=0; ptui_loginuin=1074566721; person_id_bak=5881015637151283; person_id_wsbeacon=5920911274348544; wsreq_logseq=341295039',
            'origin': 'https://h5.weishi.qq.com',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4195.1 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        rejson = {
            'datalvl': "all",
            'feedid': feedid,
            'recommendtype': '0',
            '_weishi_mapExt': '{}'
        }
        # https://h5.weishi.qq.com/webapp/json/weishi/WSH5GetPlayPage?t=0.5193563274078428&g_tk=
        # first_url='https://h5.weishi.qq.com/webapp/json/weishi/WSH5GetPlayPage?t={}&g_tk='.format(random.random())
        first_url = 'https://h5.weishi.qq.com/webapp/json/weishi/WSH5GetPlayPage'
        response = requests.post(first_url, headers=headers, json=rejson)
        result = response.json()
        # print(result)
        video_url = result['data']['feeds'][0]['video_url']
        print(video_url)

        return video_url

    @staticmethod
    def second_requset(video_url):
        video = requests.get(video_url)
        flag = video.status_code

        return flag, video


if __name__ == '__main__':
    url_text = input("请输入你要去水印的抖音短视频链接：")

    # while True:
    #     mid, video_name = GetKuaishouVideo.compile_name_url(url_text)
    #     second_url = GetKuaishouVideo.first_request(mid)
    #     third_url = GetKuaishouVideo.second_request(second_url)
    #     flag, video = GetKuaishouVideo.third_request(third_url)
    #     if flag == 200:
    #         GetKuaishouVideo.save_video(video_name, video)
    #         break
    #     print('{:-^50}'.format('请求失败，重新请求！'))

    # while True:
    #     mid, video_name = GetDouyinVideo.compile_name_url(url_text)
    #     if mid is None or video_name is None:
    #         break
    #     params = GetDouyinVideo.first_request(mid)
    #     play_url = GetDouyinVideo.second_request(params)
    #     third_url = GetDouyinVideo.third_request(play_url)
    #     flag, video = GetDouyinVideo.fourth_request(third_url)
    #     print('返回的标记和视频链接', flag, video)
    #     if 403 != flag:
    #         GetDouyinVideo.save_video(video_name, video)
    #         break
    #
    #     print('{:-^50}'.format('请求失败，重新请求！'))
