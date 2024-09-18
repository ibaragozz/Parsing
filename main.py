import requests

responce = requests.get("https://google.com/")
print(responce.status_code)
print(responce.ok)