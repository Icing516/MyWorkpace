#coding:utf-8

import requests
import urllib2

url = 'http://www.jycinema.com/frontUIWebapp/appserver/cinCinemaFilmViewService/findFilm'
head = {'Host': 'www.jycinema.com',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

param ={'params':'''{"type":"queryFilm","cityName":"深圳市","cinemaId":"","statusRE":"RELEASE","channelCode":"J0002","channelId":"3"}'''}
# sess = requests.session()
# sess.headers = head
# resp = sess.post(url, data=param)
# print resp.content
res1 = requests.post(url, data=param, headers=head)
print res1.content