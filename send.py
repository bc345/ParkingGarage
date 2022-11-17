import requests 

url = "https://seniorproject.pythonanywhere.com/uploader"

with open('outputwork.txt', 'rb') as f:
    r = requests.post(url, files={'file': f.read()})
