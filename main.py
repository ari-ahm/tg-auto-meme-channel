from telebot_router import TeleBot
import json

app = TeleBot(__name__)
env = json.load(open("env.json"))

if __name__ == "__main__":
    app.config["api_key"] = env["tg-api-key"]
    print(app.send_message(env["tg-channel-id"], "dalam"))