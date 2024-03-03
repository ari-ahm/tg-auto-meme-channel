from telebot import TeleBot
import json

env = json.load(open("env.json"))
app = TeleBot(env["tg-api-key"])

if __name__ == "__main__":
    app.send_message(env["tg-channel-id"], "salam")