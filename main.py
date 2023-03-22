from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
owner_id = os.environ["OWNER_ID"]
url = os.environ["URL"]
upload_file_key = os.environ["UPLOAD_KEY_FILE"]
secret_key = os.environ["SECRET_KEY"]
secret_value = os.environ["SECRET_VALUE"]

def is_owner(update):
    allowed = False
    user = update.message.from_user
    if user.id == int(owner_id):
        allowed = True
    return allowed

def upload_file(update, context):
    if(is_owner(update)):
        try:
            with open(update.message.document.file_name, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)

            files = {upload_file_key: open(update.message.document.file_name, 'rb')}
            data = {secret_key: secret_value}
            r = requests.post(url, files=files, data=data)
            os.remove(update.message.document.file_name)
            context.bot.send_message(chat_id=update.message.chat_id, text="File uploaded successfully.")
        except Exception as e:
            context.bot.send_message(chat_id=update.message.chat_id, text="Something went wrong:\n"+str(e))
    else:
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text='You are not the owner.')

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello")

def main():
    updater = Updater(telegram_bot_token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(MessageHandler(Filters.document, upload_file))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
