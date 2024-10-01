import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://kaluga.hh.ru/vacancies/programmist?customDomain=1")

time.sleep(3)

vacancies = browser.find_elements(By.CLASS_NAME, "vacancy-info--umZA61PpMY07JVJtomBA")
print (vacancies)

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_3-0-15 magritte-text_style-primary___AQ7MW_3-0-15 magritte-text_typography-title-4-semibold___vUqki_3-0-15').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_3-0-15 magritte-text_style-primary___AQ7MW_3-0-15 magritte-text_typography-label-3-regular___Nhtlp_3-0-15').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_3-0-15 magritte-text_style-primary___AQ7MW_3-0-15 magritte-text_typography-label-1-regular___pi3R-_3-0-15').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.Biyib').get_attribute('href')
    except:
        print('Error detected!')
        continue

    parsed_data.append([title, company, salary, link])

browser.quit()

with open("hh_hw19.csv", 'w', newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата','Ссылка на вакансию'])
    writer.writerows(parsed_data)