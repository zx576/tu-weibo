#coding=utf-8

# 本文件包含了请求网页的方法

from settings import UA,COOKIES,PROXIES
import requests
import random

class Req:

	# 使用单例模式
	_instance = None
	def __new__(cls):
		if cls._instance is None:
			Req._instance = object.__new__(cls)
		return cls._instance

	def __init__(self):
		self.headers = {'Host':'weibo.com',
						'Pragma':'no-cache',
						'Upgrade-Insecure-Requests':'1',
						}

	# 请求网页
	# 构造 header 和 proxy 进行请求
	# 如果 请求失败则删除代理重新请求一次
	# 请求 5 次失败，直接返回 None
	def _req_url(self, url, error=0):

		ua = random.choice(UA)
		cookie = random.choice(COOKIES)
		# proxy = random.choice(PROXIES)
		proxy = None

		header = self.headers
		header['User-Agent'] = ua
		header['Cookie'] = cookie

		req = requests.get(url, headers=header, proxies=proxy, timeout=5)
		try:
			assert req.status_code == 200
			return req
		except Exception as e:
			print('错误信息：{}'.format(e))
			if error == 5:
				print('超出请求上限')
				return

			PROXIES.remove(proxy)
			error += 1
			return self._req_url(url, error)

	def req_url(self, url):

		return self._req_url(url)





