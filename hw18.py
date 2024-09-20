# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# выйти из программы

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

def input_req():
    global browser
    req = input('Введите запрос: ')
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    assert "Википедия" in browser.title

    search_box = browser.find_element(By.ID, 'searchInput')
    search_box.send_keys(req)
    search_box.send_keys(Keys.RETURN)
    choice()

def list_paragraphs():
    for el in browser.find_elements(By.CLASS_NAME, "mw-search-result-heading"):
        print(el.text)
        # time.sleep(5)

def another_choice():
    link = browser.find_element(By.CSS_SELECTOR, "div.hatnote.navigation-not-searchable a").get_attribute("href")
    browser.get(link)
    # time.sleep(5)

def choice():
    choice = int(input('1. Листать параграфы текущей статьи\n2. Перейти на одну из связанных страниц\n'))

    if choice == 1:
        list_paragraphs()
    elif choice == 2:
        another_choice()

input_req()

