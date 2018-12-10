#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import urllib3
import requests
import re
from lxml import etree


# 数据保存到文件
def string_list_save(save_path, file_name, slist):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path + '/' + file_name + '.txt'
    with open(path, 'w+', encoding='utf-8') as fp:
        for s in slist:
            # print('%s\t\t%s\n' % (s[0].encode("utf8"), s[1].encode("utf8")))
            # print(s[0].__str__(),s[1].encode('utf-8'))
            fp.write('%s\t\t%s\n' % (s[0], s[1]))


def page_info(mypage):
    """  regex  """
    mypage_info = re.findall(
        r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', mypage,
        re.S)
    return mypage_info


def new_page_info(new_page):
    """ xpath """
    dom = etree.HTML(new_page)
    new_items = dom.xpath('//tr/td/a/text()')
    new_urls = dom.xpath('//tr/td/a/@href')
    assert (len(new_items) == len(new_urls))
    return zip(new_items, new_urls)


def spider(url):
    i = 0
    print('downloading %s' % url)
    mypage = requests.get(url).content.decode('gbk')
    mypage_results = page_info(mypage)
    save_path = u"网易新闻抓取"
    file_name = str(i) + "_" + u"新闻排行榜"
    string_list_save(save_path, file_name, mypage_results)
    i += 1
    for item, url in mypage_results:
        print("downloading %s" % url)
        new_page = requests.get(url).content.decode("gbk")
        new_page_results = new_page_info(new_page)
        file_name = str(i) + "_" + item
        string_list_save(save_path, file_name, new_page_results)
        i += 1


if __name__ == '__main__':
    print('start')
    start_url = "http://news.163.com/rank/"
    spider(start_url)
    print('end')
#
# print('戴荣'.__str__())

