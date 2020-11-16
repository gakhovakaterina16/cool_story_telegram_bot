import logging
import settings
from telegram.ext import (Updater, CommandHandler, 
                          MessageHandler, Filters, ConversationHandler,
                          CallbackQueryHandler)
from handlers import (greet_user, talk_to_me, send_monet_pic)
from weather import weather_start, get_weather
from nums_info import (nums_start, get_info_type, 
                       get_nums_facts)
from get_news import final_get_news


logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher

    weather = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Погода сейчас)$'),
                                     weather_start)],
        states={'get_weather': [MessageHandler(Filters.text, 
                                             get_weather)]},
        fallbacks=[]
    )

    nums_info = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Интересное о числах)$'),
                                                   nums_start)],
        states={'info_type': [MessageHandler(Filters.text,
                                             get_info_type)],
                'nums_info': [MessageHandler(Filters.text,
                                             get_nums_facts)]                                                       
                },
        fallbacks=[]
    )

    dp.add_handler(weather)

    dp.add_handler(nums_info)

    dp.add_handler(CommandHandler('start', greet_user,
                                  pass_user_data=True))
    dp.add_handler(CommandHandler('monet', send_monet_pic,
                                  pass_user_data=True))                         
    dp.add_handler(MessageHandler(Filters.regex('^(Даёшь Моне!)$'),
                                  send_monet_pic, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('^(Новость)$'),
                                  final_get_news, pass_user_data=True))                                  
    dp.add_handler(MessageHandler(Filters.text, talk_to_me,
                                  pass_user_data=True))
    dp.add_handler(CallbackQueryHandler(get_nums_facts, pattern='^(nums_type|)'))

    logging.info('The bot has started!')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
