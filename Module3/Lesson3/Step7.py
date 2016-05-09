import re
from urllib.parse import urlparse, urlsplit

html_doc = """
<a href="http://stepic.org/courses">
<a href="ftp://www.mya.ru">
<a href='https://stepic.org'>
<a link href='http://neerc.ifmo.ru:1345'>
<a target="blank" href='http://sasd.ifmo.ru:1345'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="../some_path/index.html">
<a href="https://www.ya.ru">
<a href="ftp://mail.ru/distib" >
<a href="bya.ru">
<a href="http://www.ya.ru">
<a href="www.kya.ru">
<a href="../skip_relative_links">
<a href="http://stepic.org/courses">
<a class ="hello" href= "http://ftepic.org/courses" id="dfdf">
<p class ="hello" href= "http://dtepic.org/courses">
<a class ="hello" href = "http://a.b.vc.ttepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href ="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href ="www.ya.ru">
<a href="../skip_relative_links">
<link rel="image_src" href="https://examaple.org/files/6a2/72d/e09/6a272de0944f447fb5972c44cc02f795.png" />
<a href="http://www.gtu.edu.ge/index_e.htm" target="_top">Georgian Technical University</a>﻿

"""
sites = set()

pattern1 = r'<a.*?href=[\'"](.*?)[\'"].*?>'
pattern2 = r'.*?://'
pattern3 = r'\.+'
for link in re.findall(pattern1, html_doc):
    if not re.match(pattern2, link) and not re.match(pattern3, link):
        link = 'http://'+link
    parsed_uri = urlsplit(link)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    #print(domain)
    if domain:
        sites.add(domain.split(':')[0])

for i in sorted(sites):
    print(i)
