# Parse XML file to find sum of comments

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter url:')
print('Retrieving', url)
urlhandle = urllib.request.urlopen(url)
data = urlhandle.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
print(results)

sums = 0
for comment in results:
	sums = sums + int(comment.find('count').text)

print('count', len(results))
print('sum', sums)