#coding:utf-8

import random
import copy

class Caipiao(object):
    def __init__(self):
        self.a = []
        self.b = []
        self.c = []

    def new(self):
        self.a = []
        for i in range(0, 6):
            self.a.append(random.randint(1, 33))
        for i in range(0, 2):
            self.a.append(random.randint(1, 16))
        # print self.a
        # self.b = copy.copy(self.a)
        self.b.append(self.a)
        print self.b
        # return self.b

    def add(self):
        self.new()
        # self.b.append(self.a)
        self.b.append(self.new())
        # print self.b

    def dayin(self):
        self.new()
        print self.b

    def delete(self):
        self.new()
        num1=input("请输入要删除的编号：")
        del self.b[num1-1]
        print self.b

    def xiugai(self):
        num2=input("请输入要修改的编号：")
        self.b[num2 - 1]=self.new()
        print self.b


    def exit(self):
        if (len(self.b))==0:
            print ("请问是否退出(Y/N):")
            s1=input("")
            if s1=='Y':
                exit()
        else:
            exit()

    def main(self):
        self.new()
        str=input("请选择需要操作的按钮(1新增、2打印、3删除、4修改、5退出):")
        if str==1:
            f1 = Caipiao().add()
        elif str==2:
            f2 = Caipiao().dayin()
        elif str ==3:
            f3 = Caipiao().delete()
        elif str==4:
            f4 = Caipiao().xiugai()
        elif str==5:
            f5 = Caipiao().exit()

if __name__ == '__main__':
    Caipiao().main()

# a = []
# b = []
# for i in range(0, 6):
#     a.append(random.randint(1, 33))
#     print a[i]
# for i in range(0, 2):
#     b.append(random.randint(1, 16))
#     print b[i]

'''
1.请使用python实现一个计算阶乘的函数
'''
#计算阶乘
# d =1
# num = input("请输入一个整数：")
# for i in range(1,num+1):
#     d = d*i
# print ("%d 的阶乘是 %d" %(num,d))