import logging
import settings
from telegram.ext import (Updater, CommandHandler, 
                          MessageHandler, Filters)
from handlers import (greet_user, talk_to_me, send_monet_pic,
                      get_contact, get_location, change_smile)


logging.basicConfig(filename='bot.log', level=logging.INFO)


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
