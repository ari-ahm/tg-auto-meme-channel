from telebot import TeleBot
from telebot import apihelper
import requests
import json

from posts import joke

env = json.load(open("env.json"))
app = TeleBot(env["secret"]["tg-api-key"])
apihelper.proxy = env["proxy"]
rd_auth = requests.auth.HTTPBasicAuth(env["secret"]["reddit-client-id"], env["secret"]["reddit-secret-key"])
rd_login_data = {'grant_type': 'password',
        'username': env["secret"]["reddit-username"],
        'password': env["secret"]["reddit-password"]}
rd_headers = {'User-Agent': 'ImitationBot/0.0.1'}
rd_login_res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=rd_auth, data=rd_login_data, headers=rd_headers, proxies=env["proxy"])
rd_login_token = rd_login_res.json()['access_token']
rd_headers = {**rd_headers, **{'Authorization': f"bearer {rd_login_token}"}}
# print(requests.get('https://oauth.reddit.com/r/python/hot', headers=rd_headers, proxies=env["proxy"]).text)


if __name__ == "__main__":
    joke.post(app, env)