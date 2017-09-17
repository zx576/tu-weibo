#coding=utf-8

# 测试文件
import bs4

from models import Testitem
from utils import process_time
from req import Req
from clean import Clean
from models import Aikeke


class TestDB:
	@process_time
	def test_testitem(self):
		# 测试新建
		Testitem.create(
			field1='v',
			field2=9
			)


class TestRep:

	def __init__(self):
		self.r = Req()

	def test_requrl(self):
		url = 'http://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&profile_ftype=1&is_all=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__21&id=1005051402400261&script_uri=/fly51fly&feed_type=0&page=1&pre_page=1&domain_op=100505&__rnd=1505205474083'
		res = self.r.req_url(url).json()
		soup = bs4.BeautifulSoup(res['data'])

		# print(soup.prettify())
		with open('soup.html', 'w') as f:
			f.write(soup.prettify())


class TestClean:

	def __init__(self):

		self.c = Clean('201709')

	def test_ana_normal(self):

		self.c._dispatch()


class TestAikeke:

	def test_is_saved(self):
		query = Aikeke.select()
		for i in query[:10]:
			print(i.content, i.url)



if __name__ == '__main__':
	# tdb = TestDB()
	# tdb.test_testitem()
	# trp = TestRep()
	# trp.test_requrl()
	tc = TestClean()
	tc.test_ana_normal()
	# pass
	# ta = TestAikeke()
	# ta.test_is_saved()


