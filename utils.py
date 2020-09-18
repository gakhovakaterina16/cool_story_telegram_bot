import requests
import settings
from emoji import emojize
from random import choice
from telegram import ReplyKeyboardMarkup, KeyboardButton

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def get_keyboard():                            
    greet_keyboard = ReplyKeyboardMarkup(
                                         [
                                          ['Даёшь Моне!', 'Погода сейчас'],
                                          ['Интересное о числах'], ['Новость']
                                         ], resize_keyboard=True
                                         )
    return greet_keyboard


def weather_by_city(city_name):
    weather_url = 'http://api.openweathermap.org/data/2.5/weather'
    querystring = {
        'q': city_name,
        'APPID': settings.API_KEY_WEATHER
    }
    result = requests.get(weather_url, params=querystring)
    info = result.json()
    weather_main = info['weather'][0]['main'].lower()
    temp_C = round(info['main']['temp'] - 273.15)
    reply = f'{city_name.capitalize()}: {weather_main}, {temp_C}°C'
    return reply

def en_ru_translation(word_en):
    translation_url = 'https://api.mymemory.translated.net/get'
    params = {
        'q': word_en,
        'langpair': 'en|ru',
    }
    result = requests.get(translation_url, params=params)
    info = result.json()
    return info['responseData']['translatedText']

def nums_facts(num, num_type):
    url = 'http://numbersapi.com/'
    result = requests.get(f'{url}{num}/{num_type}')
    reply = bytes.decode(result.content, encoding='utf-8')
    return reply
