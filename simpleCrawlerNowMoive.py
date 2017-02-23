#coding:utf-8

import re
import requests
import json
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class TodayMovice(object):
    '''获取金逸影城当日影视'''
    def __init__(self):
        self.url ='http://www.jycinema.com/frontUIWebapp/appserver/cinCinemaFilmViewService/findFilm'
        self.timeout =5
        self.fileName = './todayMoive.txt'
        '''内部变量定义完毕'''
        self.head ={'Host': 'www.jycinema.com',
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        self.param = {
            'params': '''{"type":"queryFilm","cityName":"深圳市","cinemaId":"","statusRE":"RELEASE","channelCode":"J0002","channelId":"3"}'''}
        self.getMoiveInfo()

    def getMoiveInfo(self):
        req = requests.post(self.url, data=self.param, headers=self.head)
        # print req.content
        result = req.content
        json_result = json.loads(result)
        film1 = json_result['data']

        for film in film1:
            print film['filmName']

        with open(self.fileName,'w') as fp:
            for film in film1:
                film = str(film['filmName'])
                fp.write(film+'\n')

if __name__ =="__main__":
    tm = TodayMovice()