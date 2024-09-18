import requests


params = {
    'userID': '1'
}

responce = requests.get("https://jsonplaceholder.typicode.com/posts?userID=1", params=params)


print(responce.text)