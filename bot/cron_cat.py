import os
import time
import requests 
import telegram
from telegram import Update, User, InputMediaPhoto
from json import *
import config
media_group = []
chat_id = config.channel_id
telegram_token = config.telegram_token

def send_photo(chat_id, image_path, image_caption="Have a good day :3"):
    data = {"chat_id": chat_id, "caption": image_caption, "photo": image_path}
    url = "https://api.telegram.org/bot%s/sendPhoto" % telegram_token
    ret = requests.post(url, data=data)
    return ret.json()

random_photo = "http://theoldreader.com/kittens/600/400"+"?ts=" + str(time.time())
r = send_photo (chat_id, random_photo)
print (r)