import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://tomsk.hh.ru/vacancies/programmist")

time.sleep(3)

vacancies = browser.find_elements(By.CLASS_NAME, "vacancy-card--H8LvOiOGPll0jZvYpxIF")
print (vacancies)

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
    except:
        print('Error detected!')
        continue

parsed_data.append([title, company, salary, link])
browser.quit()

with open("hh.csv', 'w',newline=", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата','Ссылка на вакансию'])
    writer.writerows(parsed_data)