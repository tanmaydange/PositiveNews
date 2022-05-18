# Positive News of the day

As our Honorable President Dr. APJ Abdul Kalam had once said that news papers

_"Why can’t you carry positive news on page 1? The front pages of all newspapers I see are crammed with news of scandals, crime and death. It is better to give good news to help people begin their day with hope"_

_"A man or a woman should smile in the morning. Don't make
him or her unhappy."_

[ News Link](https://www.news18.com/news/india/give-your-readers-positive-reports-kalam-461287.html)


These two quotes of our Ex President are the motivation behind this App.

## Mission 
This App has a sole purpose. Deliver positive news of the day so that the reader can start the day on a positive note.

## Design
* This Application is written in Python.
* This App will subscribe to RSS feeds.
* RSS Feeds will be configurable in config file.
* The title will be passed through sentiment analysis Algorithm to get score.
* The positive scored news will be selected.
* The app will send message on telegram so that there is no need for reader to install any application.

## Python Version:
* Python 3.6.9

## Python Libraries
* feedparser
* python-telegram-bot
* requests
* telebot

## How to use?

1. Checkout the code from github.
2. Run the script. This will create a python virtual environment and install all the required pip packages
`./init_script.sh init`
3. If you want to run sentiment analysis locally.
    
    3.a. Pull the docker image
`docker pull deepaiorg/sentiment-analysis`
    
    3.b. Run the docker container.
`sudo docker run --rm -it -e MODE=http -p 5000:5000 deepaiorg/sentiment-analysis`
    
    3.c. Test the docker container by sending a test message.
`curl  -F 'text=he team won the match' http://localhost:5000/`
4. If you want to use DEEP AI API then create a login and obtain API KEY.

    4.a.  Test your API Key by the following
`curl -F 'text=the team won the match' -H 'api-key:quickstart-QUdJIGlzIGNvbWluZy4uLi4K' https://api.deepai.org/api/sentiment-analysis`
5. Configure Telegram Bot by following the
[steps.](https://www.geeksforgeeks.org/send-message-to-telegram-user-using-python/)

6. Create a configuration File
```
[TelegramSection]
api_id=
api_hash=
token=
phone=

[SentimentSection]
api_endpoint=https://api.deepai.org/api/sentiment-analysis
api_endpoint_local=http://localhost:5000/
api_key="quickstart-QUdJIGlzIGNvbWluZy4uLi4K"

[UrlSection]
url_list=http://syndication.indianexpress.com/rss/latest-news.xml,https://timesofindia.indiatimes.com/rssfeedstopstories.cms,https://www.thehindu.com/news/feeder/default.rss,https://newsonair.gov.in/Top_rss.aspx
```

7. Run the application
`python src/GoodNewsApp.py`


## References
[DeepAI Sentiment Analysis](https://deepai.org/machine-learning-model/sentiment-analysis)

[SENTIMENT ANALYSIS DOCKER CONTAINER](https://hub.docker.com/r/deepaiorg/sentiment-analysis)

