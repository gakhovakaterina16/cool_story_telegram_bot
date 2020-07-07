import logging
import settings
from emoji import emojize
from glob import glob
from random import randint, choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup


logging.basicConfig(filename='bot.log', level=logging.INFO)


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    greet_keyboard = ReplyKeyboardMarkup([['Даёшь Моне!', 'Поменять смайлик!']])
    text = f'Привет! {context.user_data["emoji"]}'
    update.message.reply_text(text, reply_markup=greet_keyboard)


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    text = update.message.text
    update.message.reply_text(f'Привет, {username} {context.user_data["emoji"]}!\
                              Ты написал: {text}')


def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введите целое число'
    update.message.reply_text(message)


def send_monet_pic(update, context):
    monet_pics_list = glob('images/monet*.jp*g')
    monet_pic_filename = choice(monet_pics_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id,
                           photo=open(monet_pic_filename, 'rb'))


def play_random_numbers(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if user_number > bot_number:
        message = f'Ты загадал {user_number}, я загадал {bot_number}.\n \
            Ты выиграл!'
    elif user_number < bot_number:
        message = f'Ты загадал {user_number}, я загадал {bot_number}. \n \
        Я выиграл!'
    else:
        message = f'Ты загадал {user_number}, я загадал {bot_number}. Ничья!'
    return message


def change_smile(update, context):
    if 'emoji' in context.user_data:
        del context.user_data['emoji']
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Твой новый смайлик: {context.user_data["emoji"]}')



def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('guess', guess_number, pass_user_data=True))
    dp.add_handler(CommandHandler('monet', send_monet_pic, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('^Даёшь Моне!$'), send_monet_pic, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('^Поменять смайлик!$'), change_smile, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    logging.info('The bot has started!')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
