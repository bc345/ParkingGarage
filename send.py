import requests             # may have to pip install requests library

url = "https://seniorproject.pythonanywhere.com/uploader"

with open('outputwork.txt', 'rb') as f:                 #change text file name to the name of the output file from the c++ code
    r = requests.post(url, files={'file': f.read()})
