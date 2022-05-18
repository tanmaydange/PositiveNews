import feedparser
import requests
from News import News
from telegram_util import publish_telegram
import configparser
import logging

logging.basicConfig( level=logging.INFO,  filename="app.log")

TEXT_KEY='text='
CONTENT_KEY='Content-Type'
URL_ENCODED_VALUE="application/x-www-form-urlencoded"
HEADER_API_KEY='api-key'
config=configparser.RawConfigParser()
config.read("config.properties")

def check_sentiment(title):

    API_ENDPOINT = config.get('SentimentSection','api_endpoint_local')
    API_KEY_VALUE = config.get('SentimentSection','api_key')
    
    data =TEXT_KEY+ title
    headers = {HEADER_API_KEY:API_KEY_VALUE, CONTENT_KEY:URL_ENCODED_VALUE}

    return requests.post(url = API_ENDPOINT, data = data.encode('utf-8'), headers=headers).text


def fetch_news(url):
    NewsFeed = feedparser.parse(url)
    news_list= []

    for entry in NewsFeed.entries:
        news_obj = News()
        news_obj.set_title(entry['title'])
        news_obj.set_summary(entry['summary'])
        news_obj.set_link(entry['link'])
        news_obj.set_published_date(entry['published'])
        news_obj.set_sentiment(check_sentiment(entry['title']))
        news_list.append(news_obj)

    return news_list

def filter_positive(news_list):
    postive=[]
    for news_obj in news_list:
        logging.debug(news_obj.get_title())
        logging.debug(news_obj.get_sentiment())  #For debugging
        if (news_obj.get_sentiment() == "[\"Positive\"]" ):
            postive.append(news_obj)
    return postive


def main():
    url_list=config.get('UrlSection','url_list').split(sep=",")
    news_list=[] 
    for url in url_list:
        news_list.extend(fetch_news(url))

    positive_news=filter_positive(news_list)

    news_string = ""
    for news_obj in positive_news:
        news_string +="\n<a href=" + news_obj.link + ">"+ news_obj.title+"</a>"
        news_string +="\n" + news_obj.summary
        news_string +="\nPublished : " + news_obj.published_date
        news_string +="\n"

    publish_telegram(news_string)


if __name__=="__main__":
    main()