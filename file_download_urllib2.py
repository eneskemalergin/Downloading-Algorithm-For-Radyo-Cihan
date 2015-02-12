# Let's create a function that downloads a file, and saves it locally.
   
# Info needed:
# file name
# base url
# program_name
# topic_name
# file_number
# extension (default = ".mp3")
def download(base_url, program_name, topic_name, file_name, file_number, extension = ".mp3"):
        from urllib2 import Request, urlopen, URLError, HTTPError
	import os
	# Checks the first path of a directory.
        base_path = "C:/Users/Pc-41/Desktop"
        directory_one  = base_path + '/' + program_name  
        if not os.path.exists(directory_one):
            os.makedirs(directory_one)
            print("New directory created...")
        else:
            print("You already have specified directory...")
        
        # Checkst the second level path of a directory.
        directory_two = directory_one + '/' + topic_name 
        if not os.path.exists(directory_two):
            os.makedirs(directory_two)
            print("New directory created...")
            return(directory_two)
        else:
            print("You already have specidied directory...")                 
            return(directory_two) 
                        
        
	url = base_url + "%252F" + program_name + "%252F" + topic_name + "%252F" + file_name + file_number + extension
	# Makes the request.
	req = Request(url)
	
	# Open the url
	try:
		f = urlopen(req)
		print "downloading " + url
		save_name = file_name + file_number + extension
		# Open our local file for writing
		local_file = open(save_name, "w" + "b")
		
		#Write to our local file
		local_file.write(f.read())
		local_file.close()
		
	#handle errors
	except HTTPError, e:
		print "HTTP Error:",e.code , url
	except URLError, e:
		print "URL Error:",e.reason , url

# Checks the existency of a url...
# There is a bug or website that I test has a problem.
"""def exists(path):
    import requests
    r = requests.head(path)
    return r.status_code == requests.codes.ok
"""
number_list = ["%.2d" % i for i in range(62)]
for j in range(len(number_list) - 1):
    string_number = str(number_list[j])
    if string_number == "00":
        continue
    else:
        download('http://www.radyocihan.com/download/mp3/%252Fuploads%252Faudio', 'sorular-ve-cevaplar', 'birlestirilmis-s-c',
    'sorular-ve-cevaplar-', string_number, '.mp3')
print "All done!"
    
# Adding zero
str(3).zfill(2)


