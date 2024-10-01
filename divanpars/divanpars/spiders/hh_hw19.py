import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://tomsk.hh.ru/vacancies/programmist")

time.sleep(3)

vacancies = browser.find_element(By.CLASS_NAME, "vacancy-card--hhzAtjuXrYFMBMspDjrF")
print (vacancies)

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.serp-item__title-text').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-serp__vacancy-employer-text').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_3-0-15').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-2').get_attribute('href')
    except:
        print('Error detected!')
        continue

    parsed_data.append([title, company, salary, link])
    
browser.quit()

with open("hh.csv', 'w',newline=", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата','Ссылка на вакансию'])
    writer.writerows(parsed_data)