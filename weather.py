import requests
import settings
from telegram.ext import ConversationHandler
from utils import weather_by_city, en_ru_translation


def weather_start(update, context):
    update.message.reply_text('Введите название города')
    return 'get_weather'


def get_weather(update, context):
    city_name = update.message.text
    weather_en = weather_by_city(city_name)
    weather_ru = en_ru_translation(weather_en)
    update.message.reply_text(weather_ru)
    return ConversationHandler.END
