import os
import time
import logging
from datetime import datetime
import telegram
from telegram import Update, User, InputMediaPhoto
from telegram.ext import (
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    filters
)
from telegram.constants import ParseMode, ChatAction

import config

# setup
logger = logging.getLogger(__name__)

HELP_MESSAGE = """Commands:
⚪ /cat – Give you a picture

Also i have a cat streaming channel - @Yesiamacat_channel.
CATS EVERY HOUR 🔥
----
Owner – @Tipo_4ek
"""

async def start_handle(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    reply_text = "Hi! I can drop you a cat :)"
    reply_text += HELP_MESSAGE
    await update.message.reply_text(reply_text, parse_mode=ParseMode.HTML)

async def cat_handle(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    media_group = []
    cat_media_urls = ["http://theoldreader.com/kittens/600/400/", "http://theoldreader.com/kittens/600/400/", "http://theoldreader.com/kittens/600/400/"]

    for url_cat in cat_media_urls:
        print ("url is" + url_cat)
        media_group.append(InputMediaPhoto(media=url_cat + "?ts=" + str(time.time()), caption="Have a good day :3"))
    try:
        await update.message.reply_media_group(media_group)
    except Exception as e:
        await update.message.reply_text("cats are sleeping. Come back later")
    




async def message_handle(update: Update, context: CallbackContext, message=None, use_new_dialog_timeout=True):
    user_id = update.message.from_user.id
    await update.message.reply_text("I just can give you a picture :3 - /cat")

def run_bot() -> None:
    application = (
        ApplicationBuilder()
        .token(config.telegram_token)
        .build()
    )

    # add handlers
    if len(config.allowed_telegram_usernames) == 0:
        user_filter = filters.ALL
    else:
        user_filter = filters.User(username=config.allowed_telegram_usernames)

    application.add_handler(CommandHandler("start", start_handle, filters=user_filter))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & user_filter, message_handle))
    application.add_handler(CommandHandler("cat", cat_handle, filters=user_filter))
    application.add_handler(CommandHandler("help", start_handle, filters=user_filter))
    
    # start the bot
    application.run_polling()


if __name__ == "__main__":
    run_bot()
