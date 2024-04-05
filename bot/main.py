import traceback
from pathlib import Path
from pyngrok import ngrok
from flask import Flask, request

from bot.photo_sign_recognition import photo_sign_recognition
from tg_bot import Bot


port = '5000'
# ngrok_token = "2edsh9l016jCR72oIlnzGIlXTfi_2MymbkrbwJfKyMLrq6nCj"
ngrok_token = '7192759256:AAELRCpb0LSys8NoAUYyEaCwWpbJL5rrPdw'

# Setting an auth token allows us to open multiple tunnels at the same time
ngrok.set_auth_token(ngrok_token)

# Open a ngrok tunnel to the HTTP server
public_url = ngrok.connect(port).public_url
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

app = Flask(__name__)

# Update any base URLs to use the public ngrok URL
app.config["BASE_URL"] = public_url
print(app.config["BASE_URL"])

tg_token = "6936786422:AAGYvnc8j-r9cslG-SZM5hiiGybpV8UyFuk"
bot = Bot(tg_token, app.config["BASE_URL"])
drive_dir = Path('bot_data')


def download_media(bot, message, download_path=None) -> str:
    if "photo" in message:
        file_id = message["photo"][1]['file_id']
    elif "video" in message:
        file_id = message["video"]['file_id']
    else:
        return ""
    media_path, downloaded_media = bot.get_media(file_id)
    download_path = drive_dir / media_path
    with open(download_path, 'wb') as wfile:
        wfile.write(downloaded_media)
    return str(download_path)


@app.route("/", methods=["GET", "POST"])
def receive_update():
    message = None
    if request.method == "POST":
        print(request.json)
        message = request.json["message"]
        chat_id = message["chat"]["id"]
        # photos = message.get("photo")
        uid = message["from"]["id"]
        messages = ["/start"]

        # Start command
        if "entities" in message and message["text"] == "/start" and message["entities"][0]["type"] == "bot_command":
            bot.send_message(chat_id, 'Hi! Send me your photo or video!')
        elif "photo" in message:
            try:
                target_path = download_media(bot, message)
                print(target_path)
                # TODO сделать ответ бота на фотку
                result = photo_sign_recognition(target_path)
                bot.send_message(chat_id, f'Распознанный символ: {result}')
            except Exception as e:
                print(traceback.format_exc())
                bot.send_message(chat_id, 'An error occurred, please try again!')
        elif "video" in message:
            try:
                print(download_media(bot, message))
                # TODO сделать ответ бота на видео
                bot.send_message(chat_id, 'Я что-то предсказал!')
            except Exception as e:
                print(traceback.format_exc())
                bot.send_message(chat_id, 'An error occurred, please try again!')
        else:
            bot.send_message(chat_id, 'Send me your photo or video!')

    return message


app.run()
