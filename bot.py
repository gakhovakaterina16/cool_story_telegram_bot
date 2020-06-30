import logging
from telegram.ext import Updater, CommandHandler
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь!')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == 'main':
    main()
