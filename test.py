import requests
url = 'http://numbersapi.com/'
querystring = {
    'number': 5,
    'type': 'trivia'
}
result = requests.get(f'{url}{querystring["number"]}/{querystring["type"]}')
print(bytes.decode(result.content, encoding='utf-8'))

"""
    numbers = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^Интересное о числах (en)$'),
                           numbers_start)
        ],
        states={
            'info_type': [MessageHandler(Filters.text, get_info_type)],
            'numbers_info': [MessageHandler(Filters.text, get_numbers_info)]
        },
        fallbacks=[]
    )
"""
