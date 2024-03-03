import requests
import random

joke_apis = [
    lambda : requests.get("https://api.chucknorris.io/jokes/random").json()["value"] + "\n\n#ChuckNorris"
]

def getJoke() :
    return random.choice(joke_apis)()

def post(bot, env) :
    bot.send_message(env["secret"]["tg-channel-numeric-id"], "{}\n{}".format(getJoke(), env["secret"]["tg-channel-id"]))