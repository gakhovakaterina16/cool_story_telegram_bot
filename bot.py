import logging
import settings
from emoji import emojize
from glob import glob
from random import randint, choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    smile = choice(settings.USER_EMOJI)
    smile = emojize(smile, use_aliases=True)
    update.message.reply_text(f'Привет! {smile}')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


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


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('monet', send_monet_pic))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('The bot has started!')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
