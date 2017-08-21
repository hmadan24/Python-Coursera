#Extracting data from JSON
import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter the URL:')
print('Retrieving', url)
urlhandle = urllib.request.urlopen(url)
data = urlhandle.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('User count:', len(info['comments']))

sums = 0
for item in info['comments']:
	sums += int(item['count'])

print('sum:', sums)

