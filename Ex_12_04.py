#Find last link for a particular pos in link trail

import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
count = int(input('Enter count:'))
pos = int(input('Enter position:'))

i = 0
while i < count:
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup.find_all('a')
	url = tags[pos-1].get('href')
	print(tags[pos-1].get('href'))
	i += 1 