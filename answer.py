#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")

#闰年判断
while 1:
    print u"请输入一个年份："
    year = raw_input()
    nums = year.split('.')
    if year.isdigit() or (len(nums)==2 and nums[0].isdigit() and nums[1].isdigit() ):
        year = abs(int(float(year)))
        if (year%4==0 and year%100!=0) or year%400==0:
            print u"是闰年"
        else:
            print u"不是闰年"
        break
    else:
        print u"请输入一个数字"


#字母表输出
# alphabet = ','.join([chr(x)+chr(x+32) for x in range(65,91)])
# print alphabet
# print alphabet[::-1]

#单词提取
# str1 = "I love you,but I don't think you  are a good man!"
# print "The string length is : %d" % len(str1)

# for char in (",","!"):
#     str1 = str1.replace(char, " ")

# word_list = str1.split(" ")
# word_list = [x.upper() for x in word_list if x != '']
# print word_list



#斐波那契数列
# a = 0
# b = 1
# for x in range(100):
#     a,b = b,a+b
#     print a

