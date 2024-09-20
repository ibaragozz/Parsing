from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Глобальная переменная для хранения ссылок
links = []
next_page_exists = True  # Флаг, указывающий на наличие следующей страницы


def input_req():
    global browser
    req = input('Введите запрос: ')
    browser = webdriver.Chrome()
    browser.get(
        "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    assert "Википедия" in browser.title

    search_box = browser.find_element(By.ID, 'searchInput')
    search_box.send_keys(req)
    search_box.send_keys(Keys.ENTER)

    time.sleep(2)  # Даем время загрузить результаты поиска
    choice()


def list_paragraphs():
    global links
    global next_page_exists

    results = browser.find_elements(By.CLASS_NAME, "mw-search-result-heading")

    if not results:
        print("Результатов не найдено.")
    else:
        print("Найденные статьи:")
        start_idx = len(links) + 1  # Начинаем нумерацию с конца предыдущего списка
        for idx, el in enumerate(results, start=start_idx):
            link = el.find_element(By.TAG_NAME, "a").get_attribute("href")
            links.append(link)  # Сохраняем ссылку
            print(f"{idx}. {el.text} - {link}")
        print("\n")

    # Проверка наличия кнопки "следующая страница"
    try:
        next_page_button = browser.find_element(By.CSS_SELECTOR, 'a.mw-nextlink')
        next_page_exists = True
        print("Есть еще результаты. Введите 'next', чтобы загрузить следующие 20.")
    except:
        next_page_exists = False


def go_to_next_page():
    # Переходим на следующую страницу с результатами поиска
    try:
        next_page_button = browser.find_element(By.CSS_SELECTOR, 'a.mw-nextlink')
        next_page_url = next_page_button.get_attribute("href")
        print(f"Переход на следующую страницу: {next_page_url}")
        browser.get(next_page_url)
        time.sleep(2)  # Ожидаем загрузки следующей страницы
        list_paragraphs()  # Собираем результаты с новой страницы
    except Exception as e:
        print(f"Ошибка перехода на следующую страницу: {e}")


def another_choice():
    if not links:
        print("Сначала выберите пункт 1 для отображения списка статей.")
    else:
        try:
            choice_num = int(input(f"Введите номер статьи для перехода (1-{len(links)}): "))
            if 1 <= choice_num <= len(links):
                chosen_link = links[choice_num - 1]  # Индексация начинается с 0
                print(f"Переход на страницу: {chosen_link}")
                browser.get(chosen_link)
            else:
                print(f"Пожалуйста, выберите номер в диапазоне от 1 до {len(links)}.")
        except ValueError:
            print("Пожалуйста, введите корректный номер статьи.")


def choice():
    while True:
        user_choice = input(
            'Выберите действие:\n1. Листать параграфы текущей статьи\n2. Перейти на одну из связанных страниц\n3. Выйти из программы\n')

        if user_choice == '1':
            list_paragraphs()
            if next_page_exists:
                next_input = input(
                    "Введите 'next', чтобы загрузить дополнительные результаты, или нажмите Enter для продолжения: ")
                if next_input.lower() == 'next' and next_page_exists:
                    go_to_next_page()
        elif user_choice == '2':
            another_choice()
        elif user_choice == '3':
            print("Завершение программы.")
            browser.quit()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


input_req()
