# -*- coding: utf-8 -*-
# undone

import re

ua = ['''Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; Tablet PC 2.0; InfoPath.3; CIBA; Maxthon 2.0)''',
'''Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1''',
'''Mozilla/4.0 (compatible; MSIE 5.50; Windows 95; SiteKiosk 4.8)''',
'''Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC)''',
'''Mozilla/2.0 (compatible; MSIE 3.0B; Windows NT)''',
'''Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)''']
ua_ie = re.compile('/msie\s([\d\.]+)/')
ua_firefox = re.compile('/firefox\/([\d\.]+)/')
ua_chrome = re.compile('/chrome\/([\d\.]+)/')
ua_opera = re.compile('/opera.([\d.]+)/')
ua_safari = re.compile('/version\/([\d.]+).*safari/')


def test(uaStr):
    m = ua_ie.search(uaStr)
    if m:
        print 'windows', m.group()
