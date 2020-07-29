import requests
from settings import API_KEY, USER_EMOJI, API_KEY_WEATHER
from emoji import emojize
from random import choice
from telegram import ReplyKeyboardMarkup, KeyboardButton

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def get_keyboard():                            
    greet_keyboard = ReplyKeyboardMarkup(
                                         [
                                          ['Даёшь Моне!', 'Погода сейчас']
                                         ], resize_keyboard=True
                                         )
    return greet_keyboard


def weather_by_city(city_name):
    weather_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'APPID': API_KEY_WEATHER
    }
    result = requests.get(weather_url, params=params)
    info = result.json()
    weather_main = info['weather'][0]['main'].lower()
    temp_C = round(info['main']['temp'] - 273.15)
    return f'{city_name}: {weather_main}, {temp_C}°C'
