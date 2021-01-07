import requests
from random import choice
from bs4 import BeautifulSoup
from settings import BBC_URL
from telegram.ext import ConversationHandler

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_bbc_news(html):
    soup = BeautifulSoup(html, 'html.parser')
    news_list = soup.find('div', class_='e1t2pq2f4 css-kegltc-GridComponent-StyledGrid e57qer20')
    news_href = []    
    for a in news_list.find_all('a'):
        news_href.append('https://www.bbc.com' + a.get('href'))
    rand_news = choice(news_href)
    return rand_news

def final_get_news(update, context):
    html = get_html(BBC_URL)
    if html:
        rand_bbc_news = get_bbc_news(html)
        update.message.reply_text(rand_bbc_news)
