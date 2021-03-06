#coding=utf-8

# 本文件包含了数据模型


from peewee import *
from settings import *

db = MySQLDatabase(
                    database=NAME,
                    user=USER,
                    passwd=PASSWD,
                    host=HOST
                )


class Base(Model):
	"""docstring for ClassName"""
	class Meta:
		database = db


class Testitem(Base):

	# for test
	field1 = CharField(verbose_name='字段一')
	field2 = IntegerField(verbose_name='字段二')	


class Aikeke(Base):

	content = CharField(verbose_name='内容')
	url = CharField(verbose_name='链接')

def _check():

	db.connect()
	if not Testitem.table_exists():
		Testitem.create_table()

	if not Aikeke.table_exists():
		Aikeke.create_table()


_check()