# Test code to use beautifulsoup library

import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

url = input('Enter url:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

print(soup)