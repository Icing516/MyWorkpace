#coding:utf-8

import re
import urllib2
import requests

class TodayMovice(object):
    '''获取金逸影城当日影视'''
    def __init__(self):
        self.url = 'http://www.jycinema.com/frontUIWebapp/appserver/cinCinemaFilmViewService/findFilm'
        self.timeout =5
        self.fileName = './todayMoive.txt'
        '''内部变量定义完毕'''
        self.getMoiveInfo()
        self.headers = {'Host':'www.jycinema.com',
                        'Connection': 'keep-alive',
                        'Referer': 'http: // www.jycinema.com / frontUIWebapp / templates / default / index.html',
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    def getMoiveInfo(self,):
        req = urllib2.Request(self.url,self.headers)
        response = urllib2.urlopen(req)
        #response = requests.get(self.url,self.headers)
        print response.read()
        moiveList = re.findall('"film-title">(.*?)</span>',response.read())
        print moiveList
        with open(self.fileName,'w') as fp:
            for moive in moiveList:
                moive = self.subStr(moive)
                print(moive.decode('utf-8'))
                fp.write(moive+'\n')

    def subStr(self,st):
        st = st.replace('film-title">','')
        st = st.replace('</h3>','')
        return st

if __name__ =="__main__":
    tm = TodayMovice()