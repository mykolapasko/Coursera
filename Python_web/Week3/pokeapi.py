import requests
r = requests.get('http://pokeapi.co/api/v2/')
r = r.json()
count = 0
for item in r.keys():
	count += 1
	print str(item) + ": " +str(r[item])
print "Count is: " + str(count)