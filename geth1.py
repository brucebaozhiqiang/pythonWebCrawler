#coding=utf-8
#第一个python爬虫例子，注意整体框架格式及try except
from urllib import urlopen
from urllib2 import HTTPError,URLError
from bs4 import BeautifulSoup

def getTittle(url):
	try:
		html = urlopen(url)
	except (HTTPError, URLError) as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title

title = getTittle("http://www.pythonscraping.com/pages/page1.html")

if title == None:
	print("Title could not be found")
else:
	print(title)
