from telebot import TeleBot
from telebot import apihelper
import json

from posts import joke

env = json.load(open("env.json"))
app = TeleBot(env["secret"]["tg-api-key"])
apihelper.proxy = env["proxy"]

if __name__ == "__main__":
    joke.post(app, env)