import requests
from bs4 import BeautifulSoup
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://www.hmtwatches.store/product/6297d606-55df-44a0-9d2c-7ed811bf8e27"


def check_watch():
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text().lower()

    if "add to cart" in text:
        return True

    return False


def send_alert():
    message = "🚨 HMT Roman 58006 AVAILABLE!\nBuy now:\n" + URL

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_url, data=payload)


if check_watch():
    send_alert()
