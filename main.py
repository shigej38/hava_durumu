#!/usr/bin/env python3
#-*-coding:utf-8-*- """Windows için utf-8 yerine cp1254 yazılacak"""

from bs4 import BeautifulSoup as bs
import urllib.request as istek
import time
while True:
	url = "http://www.mynet.com/havadurumu//asya/turkiye/kayseri"
	urlOku = istek.urlopen(url)
	veri = bs(urlOku, 'html.parser')
	sicaklik = veri.find_all('span',attrs={'class':'hvDeg1'})
	print (sicaklik[0].text)
	time.sleep(2)
