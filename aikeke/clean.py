#coding=utf-8

# 本文件作用为清洗数据，存储内容

from req import Req
import queue
import bs4
import json

from utils import save_res
from models import Aikeke

class Clean(object):

	def __init__(self, date):
		self.r = Req()
		self.que = queue.Queue()

		self.root_url = 'http://weibo.com/fly51fly?is_all=1&stat_date={0}&page={1}#feedtop'
		self.ajax_url = 'http://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505& \
						is_all=1&stat_date={0}&pagebar={1}&pl_name=Pl_Official_MyProfileFeed__21& \
						id=1005051402400261&script_uri=/fly51fly&feed_type=0&page={2}&pre_page={2}& \
						domain_op=100505&__rnd=1505272050817'

		self.date = date
		# 初始添加 urls
		self._init_ipt_queue()
		# 

	def _init_ipt_queue(self):
		rt_url = self.root_url.format(self.date, 1)
		aj_urls = [self.ajax_url.format(self.date, i, 1) for i in range(2)]
		self.que.put(rt_url)
		for u in aj_urls:
			self.que.put(u)

	# 普通的网页加载
	def _ana_normal_html(self, html):
		if not html:
			return
		# 最后一个 script 标签
		soup = bs4.BeautifulSoup(html, 'lxml')
		soup_script = soup.find_all('script')[-1]
		# 拿出 json 字符串并转换
		json_res = str(soup_script.string)[8:-1]
		new_html = json.loads(json_res)['html']
		# 重新渲染一遍
		new_soup = bs4.BeautifulSoup(new_html, 'lxml')
		print(new_soup.prettify())
		# 将取出的 内容存入 html 	
		# 调试时使用方法
		with open('new_soup.html', 'w')as f:
			f.write(new_soup.prettify())
		# self._ana_html_tags(new_soup)

	# 分析网页并及时保存结果
	def _ana_html_tags(self, soup):
		# print(soup)
		soup_div = soup.find_all('div', class_="WB_text W_f14")
		# print(len(soup_div))
		for div in soup_div:
			# 博文内容
			content = list(div.stripped_strings)[0]
			# 相关链接
			a_url = div.find('a', attrs={'action-type': 'feed_list_url'})
			url = a_url['href'] if a_url else 'none'
			print(content, url)
			Aikeke.create(
				content=content,
				url=url)


	# ajax 加载的网页分析
	def _ana_ajax_html(self, html):

		pass

	def add_pages_to_que(self, maxpage):
		if not maxpage or maxpage < 2:
			return
		for i in range(2, maxpage):
			self.que.put(self.root_url.format(self.date, i))
			aj_urls = [self.ajax_url.format(self.date, j, i) for j in range(2)]
			for u in aj_urls:
				self.que.put(u)


	# 分发内容
	def _dispatch(self):

		while True:
			
			if self.que.empty():
				break

			try:
				url = self.que.get()
				page = self.r.req_url(url)
				if url.startswith('http://weibo.com/p/aj'):
					self._ana_ajax_html(page.json())
				else:
					self._ana_normal_html(page.text)

			except Exception as e:
				print(e)
				break




		

