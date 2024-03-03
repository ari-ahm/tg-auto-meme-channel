from telebot import TeleBot
import json

env = json.load(open("env.json"))
app = TeleBot(env["secret"]["tg-api-key"])

if __name__ == "__main__":
    app.send_message(env["secret"]["tg-channel-id"], "salam")