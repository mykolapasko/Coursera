import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('span')
mySum = 0
for tag in tags:
    mySum += int(tag.contents[0])
print "Sum ", mySum