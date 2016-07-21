import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter - ')
position = 18
repeat = 7
content = []
while repeat > 0:	
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	content.append(tags[position - 1].contents[0])
	target = str(tags[position - 1])
	target = re.findall(r'href="(.+)"', target)
	url = target[0]
	repeat -= 1
print content[-1]


