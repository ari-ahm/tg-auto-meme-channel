from telebot import TeleBot
from telebot import apihelper
import requests
import json

from posts import joke, redditMeme

conf = json.load(open("conf.json"))
print("[INF] Connecting to telegram api")
app = TeleBot(conf["secret"]["tg-api-key"])
apihelper.proxy = conf["proxy"]
print("[INF] Connecting to reddit api")
rd_auth = requests.auth.HTTPBasicAuth(conf["secret"]["reddit-client-id"], conf["secret"]["reddit-secret-key"])
rd_login_data = {'grant_type': 'password',
        'username': conf["secret"]["reddit-username"],
        'password': conf["secret"]["reddit-password"]}
rd_headers = {'User-Agent': 'ImitationBot/0.0.1'}
rd_login_res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=rd_auth, data=rd_login_data, headers=rd_headers, proxies=conf["proxy"])
rd_login_token = rd_login_res.json()['access_token']
conf["reddit-header"] = {**rd_headers, **{'Authorization': f"bearer {rd_login_token}"}}

print("[INF] Setup completed")

if __name__ == "__main__":
    joke.post(app, conf)
    redditMeme.post(app, conf)