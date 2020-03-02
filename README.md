# KGdownload 酷狗歌单一键下载(Mobile Size)
***

## 思路：

### 1.请求歌单
手机分享的链接是短链，如：https://t4.kugou.com/8IhBCd0wiV2 \<br>
但请求后是：https://www.kugou.com/share/zlist.html?u=1012067831&h1=29788683337423371519676878899389792699&h2=6b203ce0a8fa17bfa4b75468a196f093&listid=2&global_collection_id=collection_3_1012067831_2_0&uid=1012067831&type=0&_t=1582965370&token=506dc56fa2e4a7319fddf9cdb65080e39cb5fed18b29388d5851b4e21695a4a3&sign=c902599f4d8b2c89302ff878f8629710&chl=link\<br>
切换手机模式，即可看到歌单。\<br>
我们知道，有正则可以取得歌单\<br>
但是该网页是js动态加载的，因此我们要开发者工具切换到network下的XHR\<br>
可看到json.\<br>
json处理后得：hash和name\<br>

### 2.获取MP3真正url
url真正的url\<br>
''' python
http://trackercdn.kugou.com/i/v2/?appid=1005&pid=2&cmd=25&behavior=play&hash={hash}&key={key}
'''\<br>
key是hash+'kgcloudv2'的加盐值（别问我怎么知道）\<br>
请求后得json\<br>
再处理json得出真正url\<br>

### 下载
不用我说了吧\<br>
***

## 如何使用
1.用手机酷狗分享歌单，得短链\<br>
2.复制到浏览器，得长链\<br>
3.打开KGdownloa并复制\<br>
4.等待下载完成\<br>

