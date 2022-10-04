# -*-coding:utf8-*-
import requests



req = requests.get('https://zxsj.wanmei.com/news/index.html').text


print(req)

