from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

def mainloop():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Завершение программы...")



browser = webdriver.Chrome()
# browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")
#
# hatnotes = []
# for el in browser.find_elements(By.TAG_NAME, "div"):
#     cl = el.get_attribute("class")
#     if cl == "hatnote navigation-not-searchable":
#         hatnotes.append(el.text)
#
# print(hatnotes)
# hatnote = random.choice(hatnotes)
#
# link = browser.find_element(By.CSS_SELECTOR, "div.hatnote.navigation-not-searchable a").get_attribute("href")
#
# browser.get(link)
# time.sleep(5)





# paragraphs = browser.find_elements(By.TAG_NAME, 'p')
#
# for paragraph in paragraphs:
#     print(paragraph.text)
#     input()


# assert 'Википедия' in browser.title
# time.sleep(5)
# search_box = browser.find_element(By.ID, 'searchInput')
# search_box.send_keys('Солнечная система')
# search_box.send_keys(Keys.RETURN)
# time.sleep(5)
# a = browser.find_element(By.LINK_TEXT, 'Солнечная система')
# a.click()
# time.sleep(5)


browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/Document_Object_Model')
# browser.save_screenshot('dom.png')
time.sleep(5)
browser.get('https://en.wikipedia.org/wiki/Selenium')
time.sleep(3)
browser.refresh()
mainloop()