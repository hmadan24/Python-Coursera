#Testing a regular expression	
x = 'harshit.m@adan@musktechnologies.com'

import re
print(re.findall('\S+?@\S+?',x))