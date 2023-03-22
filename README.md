# Telegram File Uploader Bot

This is a simple Telegram bot that will accept files from users and upload them to a given URL. The bot will only accept files from the owner of the bot, and will send back the response from the URL after uploading.

## How to use it

1. Clone this repository and install the requirements.txt file.
2. Set the following environment variables:

- `telegram_bot_token`: The token of your Telegram bot. You can get it from [@BotFather](https://t.me/BotFather).
- `owner_id`: The user ID of the owner of the bot. You can get it from [@userinfobot](https://t.me/userinfobot).
- `url`: The URL where you want to upload the files. It should accept POST requests with multipart/form-data content type.
- `upload_file_key`: The key name for the file parameter in the POST request.
- `secret_key`: The key name for an optional secret parameter in the POST request. This can be used to authenticate your requests to the URL.
- `secret_value`: The value for the secret parameter in the POST request.

3. Run the main.py file and start sending files to your bot on Telegram. The bot will reply with the response from the URL after uploading each file.
