from telegram.ext import ConversationHandler
from utils import (nums_facts, en_ru_translation,
                   nums_type_inline_keyboard,
                   ru_en_choice_keyboard)


def nums_start(update, context):
    update.message.reply_text('Введите число')
    return 'info_type'


def get_info_type(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='Выберите тип информации',
                             reply_markup=nums_type_inline_keyboard())
    num = int(update.message.text)
    context.user_data['num'] = num
    return 'nums_info'


def get_nums_facts(update, context):
    update.callback_query.answer()
    fact_type = str(update.callback_query.data).replace('nums_type', '')
    if fact_type == 'math' or 'trivia':
        reply = nums_facts(context.user_data['num'], fact_type)
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id=chat_id, text=reply)   
    context.bot.send_message(chat_id=chat_id, text='перевести на русский?',
                             reply_markup=ru_en_choice_keyboard())
    update.callback_query.answer()
    print(update.callback_query.data)
    return ConversationHandler.END
