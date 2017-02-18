#coding:utf-8

class Fibonacci(object):
    '''返回一个fibonacci函数'''
    def __init__(self):
        self.fList = [0,1]
        self.main()

    def main(self):
        listLen = input('请输入fibonacci数列的长度(3——50):')
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1] + self.fList[-2])
        print('得到的fibonacci数列为:\n %s ' %self.fList)

    def checkLen(self,lenth):
        lenList = map(str,range(3,51))  #map函数，将range产生的数列以字符串的形式输出
        if lenth in lenList:
            print('输入的长度符合标准，继续运行')
        else:
            print(u'只能输入3-50，太长了不是算不出，只是没必要')
            exit()

if __name__ == '__main__':
    f = Fibonacci()