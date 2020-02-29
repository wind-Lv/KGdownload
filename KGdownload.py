#酷狗批量下载器 | 手机分享链接
import requests, json
from bs4 import BeautifulSoup
from hashlib import md5
from threading import Thread


'''
链接参数如下：

默认参数
listid默认值为 2
type默认值为 0

原链接参数
uid
sign 
_t 
global_collection_id
token

可变化参数
page
'''

#list_url = f'https://m3ws.kugou.com/zlist/list?listid=2&type=0&{uid}&{sign}&{t}&{gcid}&page={p}&{tolen}'

class kg(object):
    def __init__(self):
        iurl = input('>')
        can_list = iurl.replace('https://m3ws.kugou.com/share/zlist.html?','').split('&') 

        self.uid = can_list[5]
        self.gcid = can_list[4]
        self.t = can_list[7]
        self.token = can_list[8]
        self.sign = can_list[9]
    
    #重复无限次，直到报错
    def json(self,p):
        url = f'https://m3ws.kugou.com/zlist/list?listid=2&type=0&{self.uid}&{self.sign}&{self.t}&{self.gcid}&page={p}&{self.token}'
        self.js = json.loads(requests.get(url).text)

    #重复30次
    def mp3_url(self,x):
        hash = self.js['list']['info'][x]['hash']
        key = md5((hash+'kgcloudv2').encode('utf-8')).hexdigest()

        name = self.js['list']['info'][x]['name']
        mp3url = f'http://trackercdn.kugou.com/i/v2/?appid=1005&pid=2&cmd=25&behavior=play&hash={hash}&key={key}'
        print(mp3url)
        return name,mp3url


def download(name,mpurl):
    js = json.loads(requests.get(mpurl).text)
    url = js['url'][0].replace('\\','')
    mp3 = requests.get(url)
    with open(f'download/{name}.mp3','wb') as f:
        f.write(mp3.content)



kg = kg()
p = 1
while True:
    try:
        kg.json(p)
    except:
        break
    for i in range(30):
        name,mpurl = kg.mp3_url(i)
        download(name,mpurl)
    p += 1

#还差多线程下载
