#coding=utf-8

# 一些爬取过程中用到的工具函数

from functools import wraps
import time 

# 测试运行时间的装饰器
def process_time(func):
	@wraps(func)
	def inner(*arge, **kw):

		print(time.ctime())
		return func(*arge, **kw)
		print(time.ctime())

	return inner


# 保存返回内容的装饰器
def save_res(func):
	@wraps(func)
	def inner(*args, **kw):
		print('in dec')
		res = func(*args, **kw)
		with open('test.html', 'w')as f:
			f.write(res)

	return inner

# 延迟执行 t 秒
def delay(t):
	if not isinstance(t, int):
		t = 3
	time.sleep(t)
	def wrapfunc(func):
		@wraps(func)
		def inner(*args, **kw):
			
			return func(*args, **kw)

		return inner

	return wrapfunc

