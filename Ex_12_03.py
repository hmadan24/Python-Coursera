#Counting numbers by scraping a web page

import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all('span')


sums = 0
for tag in tags:
	num = re.findall('>([0-9]+)<', str(tag))
	print(tag, num)
	if num != []:
		sums = sums + float(num[0])
print(int(sums))