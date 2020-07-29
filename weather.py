import requests
from settings import API_KEY_WEATHER
from telegram.ext import ConversationHandler


def weather_start(update, context):
    update.message.reply_text('Введите название города')
    return 'get_weather'


def weather_by_city(city_name):
    weather_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'APPID': API_KEY_WEATHER
    }
    result = requests.get(weather_url, params=params)
    info = result.json()
    weather_main = info['weather'][0]['main']
    temp_C = round(info['main']['temp'] - 273.15)
    return f'{city_name}. {weather_main}. {temp_C}°C.'

def get_weather(update, context):
    city_name = update.message.text
    try:
        weather_reply = weather_by_city(city_name)
    except (ValueError, TypeError):
        weather_reply = 'Название города в виде: Москва'
    update.message.reply_text(weather_reply)
    return ConversationHandler.END
