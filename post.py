import urllib
import urllib2

url = 'http://10.86.0.7/post.php'
i=0
for i in range(0, 3):
	# Prepare the data
	
	values = {'msg' : '[python]' + str(i)} 
	data = urllib.urlencode(values)

	# Send HTTP POST request
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)

	html = response.read()

# Print the result
	print html
