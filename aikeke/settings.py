#coding=utf-8
# author = zhouxin
# 本文件为微博项目的设置文件
# 包含了一些基本的配置文件

import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))

# 数据库配置

NAME = 'weibo'
USER = 'labadmin'
PASSWD = 'labadmin'
HOST = 'localhost'


# 帐号cookie
COOKIES = []

# headers 

UA = [
                # safari 5.1 – MAC
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                # safari 5.1 – Windows
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                # Firefox 38esr
                'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
                # IE 11
                'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
                # IE 9.0
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
                # IE 8.0
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
                # IE 7.0
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
                # IE 6.0
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
                # Firefox 4.0.1 – MAC
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                # Firefox 4.0.1 – Windows
                'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                # Opera 11.11 – MAC
                'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
                # Opera 11.11 – Windows
                'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
                # Chrome 17.0 – MAC
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
                # 傲游（Maxthon）
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
                # 腾讯TT
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
                # 世界之窗（The World） 2.x
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                # 世界之窗（The World） 3.x
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
                # 搜狗浏览器 1.x
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
                # 360浏览器
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
                # Avant
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
                # Green Browser
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'

            ]

# 代理

PROXIES = []