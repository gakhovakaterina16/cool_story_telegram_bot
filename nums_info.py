from telegram.ext import ConversationHandler
from utils import nums_facts, en_ru_translation


def nums_start(update, context):
    update.message.reply_text('Введите число')
    return 'info_type'


def get_info_type(update, context):
    update.message.reply_text(
        'Укажите тип информации: math или trivia'
    )
    num = int(update.message.text)
    context.user_data['num'] = num
    return 'nums_info'


def get_nums_facts(update, context):
    fact_type = update.message.text
    reply = nums_facts(context.user_data['num'], fact_type)
    reply_ru = en_ru_translation(reply)
    update.message.reply_text(reply_ru)
    return ConversationHandler.END    
