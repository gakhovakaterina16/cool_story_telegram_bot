from telegram.ext import ConversationHandler
from utils import (nums_facts, en_ru_translation,
                   nums_type_inline_keyboard,
                   ru_en_choice_keyboard)


def nums_start(update, context):
    update.message.reply_text('Введите число')
    return 'info_type'


def get_info_type(update, context):
    chat_id = update.effective_chat.id
    num = int(update.message.text)
    context.user_data['num'] = num
    context.bot.send_message(chat_id=chat_id, text='Выберите тип информации',
                             reply_markup=nums_type_inline_keyboard())
    return 'nums_info'


def get_nums_facts(update, context):
    update.callback_query.answer()
    chat_id = update.effective_chat.id
    fact_type = str(update.callback_query.data).replace('nums_type', '')
    reply = en_ru_translation(nums_facts(context.user_data['num'], fact_type))
    context.bot.send_message(chat_id=chat_id, text=reply)
    return ConversationHandler.END