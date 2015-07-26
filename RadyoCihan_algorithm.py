import urllib2

def download(base, program, topic, file_name, file_number, extension):
    url = base + program + '%252F' + topic + '%252F' + file_name + file_number + extension
    name = urllib2.urlopen(url)
    output = open(file_name + file_number + extension, 'wb')
    print ("Downloading " + file_name + file_number + extension + "...")
    output.write(name.read())
    output.close()


if __name__ == '__main__':
    import os
    path = raw_input("Please Enter the Path you want to save your files:")
    os.chdir(path)

    print "Your current working directory has been changed to"
    os.getcwd()

    # Getting the necessary inputs...
    base = raw_input("Enter the base url: ")
    program = raw_input("Enter the program name: ")
    topic = raw_input("Enter the topic name: ")
    file_name = raw_input("Enter the file name: ")
    file_number = int(raw_input("Enter the upper limit number: "))
    extension1 = raw_input("Enter the extension1: ")
    extension2 = raw_input("Enter the extension2: ")
    answer =  raw_input("Would you like to start downloading (Y/y): ")

    if answer == 'Y' or answer == 'y':
        numbers_list = ['%.3d' % i for i in range(file_number)]
        for j in range(len(numbers_list)-1 , 100, -1):
            string_number = str(numbers_list[j])
            if string_number == "000":
                continue
            else:
                download(base, program, topic, file_name, string_number, extension1)
                download(base, program, topic, file_name, string_number, extension2)
    print "All Done!"

'''
Here is simple usage of an algorithm:
base = http://www.radyocihan.com/download/mp3/%252Fuploads%252Faudio%252F
program = hikmet-penceresi
topic = hikmet-penceresi
file_name = murat-kara-hikmet-penceresi-
file_number = 880
extension = -a.mp3

# http://www.radyocihan.com/download/mp3/%252Fuploads%252Faudio%252Fhikmet-penceresi%252Fhikmet-penceresi%252Fmurat-kara-hikmet-penceresi-875-b.mp3

'''
