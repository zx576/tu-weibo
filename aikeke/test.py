#coding=utf-8

# 测试文件

from models import Testitem
from utils import process_time


class TestDB:
	@process_time
	def test_testitem(self):
		# 测试新建
		Testitem.create(
			field1='v',
			field2=9
			)



if __name__ == '__main__':
	tdb = TestDB()
	tdb.test_testitem()

