import logging
import settings
from emoji import emojize
from glob import glob
from random import randint, choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton


logging.basicConfig(filename='bot.log', level=logging.INFO)


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    contact_button = KeyboardButton('Прислать контакты',
                                    request_contact=True)
    location_button = KeyboardButton('Прислать координаты',
                                     request_location=True)                                
    greet_keyboard = ReplyKeyboardMarkup(
                                         [
                                          ['Даёшь Моне!', 'Поменять смайлик!'],
                                          [contact_button, location_button]
                                         ]
                                         )
    text = f'Привет! {context.user_data["emoji"]}'
    update.message.reply_text(text, reply_markup=greet_keyboard)


def get_contact(update, context):
    print(update.message.contact)
    text = f'Готово! {get_smile(context.user_data)}'
    update.message.reply_text(text)    


def get_location(update, context):
    print(update.message.location)
    text = f'Готово! {get_smile(context.user_data)}'
    update.message.reply_text(text)   


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


def change_smile(update, context):
    if 'emoji' in context.user_data:
        del context.user_data['emoji']
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Твой новый смайлик: \n \
                              {context.user_data["emoji"]}')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user,
                                  pass_user_data=True))
    dp.add_handler(CommandHandler('monet', send_monet_pic,
                                  pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('^Даёшь Моне!$'),
                                  send_monet_pic, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('^Поменять смайлик!$'),
                                  change_smile, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact,
                                  pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location,
                                  pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me,
                                  pass_user_data=True))

    logging.info('The bot has started!')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
