#coding:utf-8


class PrintTable(object):
	'''打印九九乘法表 '''
	def __init__(self):
		print(u'开始打印9x9的乘法表格')
		self.print99()

	def print99(self):
		for i in range(1,10):
			for j in range(1,i+1):
				print('%dX%d=%2s  ' %(j,i,i*j)),
			print('\n')

if __name__ == '__main__':
    pt = PrintTable()