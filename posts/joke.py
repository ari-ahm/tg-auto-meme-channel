import requests
import random

joke_apis = [
    lambda : requests.get("https://api.chucknorris.io/jokes/random").json()["value"] + "\n\n#ChuckNorris"
]

def getJoke() :
    return random.choice(joke_apis)()

def post(bot, conf) :
    bot.send_message(conf["secret"]["tg-channel-numeric-id"], "{}\n{}".format(getJoke(), conf["secret"]["tg-channel-id"]))