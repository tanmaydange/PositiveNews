# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import configparser

def publish_telegram(message):
	config=configparser.RawConfigParser()
	config.read("config.properties")
	api_id = config.get('TelegramSection','api_id')
	api_hash = config.get('TelegramSection','api_hash')
	token = config.get('TelegramSection','token')
	phone = config.get('TelegramSection','phone')

	client = TelegramClient('session', api_id, api_hash)

	client.connect()

	if not client.is_user_authorized():
		client.send_code_request(phone)
		client.sign_in(phone, input('Enter the code: '))

	try:
		receiver = client.get_input_entity('@positive_news_dange_bot')
		client.send_message(receiver, message, parse_mode='html')
	except Exception as e:	
		print(e);

	client.disconnect()

if __name__=='__main__':
	publish_telegram("Hello World")