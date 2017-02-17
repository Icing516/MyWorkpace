#-*- coding: utf-8 -*-

class PrintTable(object):
    '''打印九九乘法表 '''

    def __init__(self):
        print(u'开始打印9x9的乘法表格')
        self.print99()

    def print99(self):
        for i in range(1, 10):
            for j in range(1, i + 1):
                print("%d*%d=%2d" % (i, j, i * j), end="  "),
            print(' ')

if __name__ == '__main__':
    pt =PrintTable()
