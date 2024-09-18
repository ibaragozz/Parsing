import requests

img = 'https://sun9-47.userapi.com/impg/WYFEJZS0p7BrM0RmZFs5Qg0ka9sW4FF3cx_SJQ/Y4ZkJhumBEQ.jpg?size=1620x2160&quality=95&sign=189551173451061bc964d7143e9fc1eb&type=album'

responce = requests.get(img)

with open('test.png', 'wb') as file:
    file.write(responce.content)