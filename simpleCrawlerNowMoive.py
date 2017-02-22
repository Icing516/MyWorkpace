#coding:utf-8

import re
import urllib2

class TodayMovice(object):
    '''获取金逸影城当日影视'''
    def __init__(self):
        self.url = 'http://www.jycinema.com/frontUIWebapp/appserver/cinCinemaFilmViewService'
        self.timeout =5
        self.fileName = './todayMoive.txt'
        '''内部变量定义完毕'''
        self.getMoiveInfo()

    def getMoiveInfo(self):
        response = urllib2.urlopen(self.url,timeout=self.timeout)
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