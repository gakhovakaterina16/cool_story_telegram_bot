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
    contact_button = KeyboardButton('Прислать контакты',
                                    request_contact=True)
    location_button = KeyboardButton('Прислать координаты',
                                     request_location=True)                                
    greet_keyboard = ReplyKeyboardMarkup(
                                         [
                                          ['Даёшь Моне!', 'Поменять смайлик!'],
                                          [contact_button, location_button]
                                         ], resize_keyboard=True
                                         )
    return greet_keyboard
