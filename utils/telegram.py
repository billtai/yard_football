from flask import current_app
from urllib.parse import urlencode
import requests

def send(message: str):
    # Gủi tin nhắn telegran
    pass
    # chat_id = current_app.config['TELEGRAM_TO']
    # bot_token = current_app.config['TELEGRAM_BOT']
    # path = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}"
    # app_name = current_app.config['TELEGRAM_APP'];
    # message = urlencode({'text': f"<b>{app_name}</b>\n{message}"})
    # requests.get(f"{path}&{message}&parse_mode=html")