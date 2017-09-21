#coding=utf-8

import csv
from models import Aikeke


class ToCsv:

	def __init__(self):
		pass

	def _insertrow(self, lst):
		with open('aikeke.csv', 'a+', encoding='utf-8', newline='')as f:
			writer = csv.writer(f)
			writer.writerow(lst)

	def _extract(self):

		# 作为示例，输出前 100 条
		query = Aikeke.select()[:500]
		for item in query:

			self._insertrow([item.content, item.url])

	def work(self):

		return self._extract()


if __name__ == '__main__':
	tc = ToCsv()
	tc.work()



