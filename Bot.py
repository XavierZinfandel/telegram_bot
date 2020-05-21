import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

PROXY = {"proxy_url": settings.proxy_url,
        "urllib3_proxy_kwargs": {"username": settings.proxy_username, "password": settings.proxy_password}}

def greet_user(update, context):
    print("Вызван старт")
    update.message.reply_text("Hi there!")

def talk(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.api_key, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk))

    logging.info("Bot has started")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
   main()
