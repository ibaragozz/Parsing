import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/category/svet"

driver.get(url)

time.sleep(3)

lights = driver.find_elements(By.CLASS_NAME, '_Ud0k')

parsed_data = []

for light in lights:
    try:
        name = light.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        link = light.find_element(By.CSS_SELECTOR, value='a.ui-GPFV8.qUioe.ProductName').get_attribute('href')
        price = light.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
    except:
        print("Произошла ошибка при парсинге!")
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open("hw19.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Наименование товара', 'Цена', 'Ссылка на товар'])
    writer.writerows(parsed_data)
