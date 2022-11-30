import requests             # may have to pip install requests library
import time
url = "https://seniorproject.pythonanywhere.com/uploader"

while True:
    with open('/home/pi/projects/output.txt', 'rb') as f:                 #change text file name to the name of the output file from the c++ code
        r = requests.post(url, files={'file': f.read()})
        print("updated")
    time.sleep(1)
