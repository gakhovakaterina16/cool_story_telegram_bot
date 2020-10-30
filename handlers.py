from glob import glob
from random import choice
from utils import (get_smile, get_keyboard, weather_by_city)


def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = f'Привет! {context.user_data["emoji"]}'
    update.message.reply_text(text, reply_markup=get_keyboard())


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    text = update.message.text
    update.message.reply_text(f'Привет, {username} {context.user_data["emoji"]}!\
                              Ты написал: {text}')


def send_monet_pic(update, context):
    monet_pics_list = glob('images/monet*.jp*g')
    monet_pic_filename = choice(monet_pics_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id,
                           photo=open(monet_pic_filename, 'rb'))
