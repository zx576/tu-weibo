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
COOKIES = [
    'SINAGLOBAL=9969846395011.81.1497235249287; UM_distinctid=15d017a3f2e61c-0f2f82a49df65-1d2a1f03-1fa400-15d017a3f2f6f6; TC-Ugrow-G0=968b70b7bcdc28ac97c8130dd353b55e; login_sid_t=b977913063a83a604e610c002dd4b4e0; TC-V5-G0=914ba011d20e5b7f25fe12574c186eda; _s_tentry=-; Apache=2198531408771.598.1505697379016; ULV=1505697379028:20:4:1:2198531408771.598.1505697379016:1505350621573; SSOLoginState=1505697398; TC-Page-G0=07e0932d682fda4e14f38fbcb20fac81; YF-Page-G0=8eed071541083194c6ced89d2e32c24a; YF-Ugrow-G0=ea90f703b7694b74b62d38420b5273df; YF-V5-G0=46bd339a785d24c3e8d7cfb275d14258; un=17740675026; cross_origin_proto=SSL; wvr=6; UOR=www.blogjava.net,widget.weibo.com,www.baidu.com; SCF=AgB5TbPtv-B0qezkkU9c1gpwMpUPJWd0skzDJ6zAHZPU_FRWXq_R4H2IitWypIeI2l8xa33vIViPjvaxWp62m_4.; SUB=_2A250x2maDeRhGeBO41QT-SvEyzSIHXVXtdxSrDV8PUJbmtAKLRbVkW97Mq5WjJxBcg3U2Vfvyz6HvS4O0A..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWd-wGLnVE0Vqpgm_2iG0yi5JpX5o2p5NHD95Qcehnceo.f1h5RWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSo5RSoz4SKn715tt; SUHB=0h1J1KtCyxwbcU; wb_cusLike_6086295808=Y',
]

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

PROXIES = [
    # {"http": "111.13.2.131:80"},
    # {"http": "61.152.81.193:9100"},
    # {"http": "162.243.18.46:3128"},
    # {"http": "183.232.65.202:3128"},
    # {"http": "219.149.46.151:3128"},
    # {"http": "121.69.3.102:8080"},
    # {"http": "111.13.109.27:80"},
    # {"http": "222.196.33.254:3128"},
    # {"http": "111.13.7.120:80"},
    # {"http": "111.13.2.138:80"},
    # {"http": "111.13.7.117:80"},
    # {"http": "111.13.7.119:80"},
    # {"http": "210.61.209.197:3128"},
    # {"http": "223.20.215.217:9000"},
    # {"http": "61.136.163.245:3128"},
    # {"http": "111.13.7.122:80"},
    # {"http": "111.13.7.123:80"},
    # {"http": "106.119.0.244:8080"},
    # {"http": "93.91.112.185:80"},
    # {"http": "120.77.255.133:8088"}
]
