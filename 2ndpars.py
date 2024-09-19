from bs4 import BeautifulSoup
import requests
from googletrans import Translator


def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()

        return {
            'english_word': english_words,
            'word_definition': word_definition
        }
    except:
        print('Error')

def word_game():
    print('Добро пожаловать в игру "Английские слова"!')
    while True:
        word_dict = get_english_words()
        word = word_dict.get('english_word')
        word_definition = word_dict.get('word_definition')
        translator = Translator()
        ru_word = translator.translate({word}, dest='ru').text.strip()
        ru_word_definition = translator.translate({word_definition}, dest='ru').text.strip()

        print(f'Значение слова - {ru_word_definition}')
        user = input('Что это за слово?')
        if user == ru_word:
            print('Правильно!')
        else:
            print(f'Неправильно. Правильное слово - {ru_word}')

        play_again = input('Хотите сыграть еще раз? (y/n)')
        if play_again.lower() != 'y':
            print('Спасибо за игру!')
            break

word_game()
