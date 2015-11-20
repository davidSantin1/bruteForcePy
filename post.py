import urllib
import urllib2
import sys, getopt

def usage():
	print "-h, --help print this message \n-u, --url set target\n-m, --mode set mode POST or GET Ex.: -m p | -m g"
def main(argv):
	url= ""
	mode= ""
	try:                                
		opts, args = getopt.getopt(argv, "u:m:", ["url", "mode"])
	except getopt.GetoptError:          
        	usage()                         
        	sys.exit(2)
	for opt, arg in opts:  
        	if opt in ("-m", "--mode"):                        		
			mode = arg	
			print(mode)		                  
        	elif opt in ("-u", "--url"):  
        		url = arg 
     
	if url == "":	
		print("--url ERROR") 	
		usage()
		sys.exit()
	if mode == "" or (mode != "p" and mode != "g"):
		print("--mode ERROR") 	
		usage()
		sys.exit()
		
	#url = 'http://10.86.0.7/post.php'
	
	for i in range(0, 3):
		# Prepare the data
	
		values = {'msg' : '[python]' + str(i)} 
		data = urllib.urlencode(values)

		# Send HTTP POST request
		req = urllib2.Request(str(url), data)
		response = urllib2.urlopen(req)

		html = response.read()

		# Print the result
		print html
if __name__ =='__main__':
	main(sys.argv[1:])
