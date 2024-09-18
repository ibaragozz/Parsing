import requests
import pprint

responce = requests.get("https://api.github.com/")
# print(responce.status_code)
# print(responce.ok)
# if responce.ok:
#     print('Запрос выполнен успешно')
# else:
#     print('Произошла ошибка при выполнении запроса')

print(responce.text)
responce_json = responce.json()
pprint.pprint(responce_json)