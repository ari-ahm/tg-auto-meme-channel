import requests
from redvid import Downloader
from os import path

def getMedia(dct) :
    if ("data" in dct and "is_video" in dct["data"] and dct["data"]["is_video"]) :
        return dct["data"]["url"]
    return None

def getName(dct) :
    if ("data" in dct and "name" in dct["data"]) :
        return dct["data"]["name"]
    return None

def post(bot, conf) :
    opt = requests.get('https://oauth.reddit.com/r/discordVideos/top', headers=conf["reddit-header"], proxies=conf["proxy"]).json()["data"]["children"]
    dl = Downloader(max_q=True)
    for i in opt :
        vidLink = getMedia(i)
        if (vidLink == None) :
            continue
        if (path.exists("downloads/{}.mp4".format(getName(i)))) :
            continue
        print(vidLink)
        dl.url = vidLink
        dl.path = "downloads/"
        dl.filename = getName(i)
        dl.proxies = conf["proxy"]
        dl.download()
        try :
            bot.send_video(chat_id=conf["secret"]["tg-channel-numeric-id"], video=open(dl.file_name, "rb"), supports_streaming=True, caption=conf["secret"]["tg-channel-id"], timeout=15*60*1000)
        except KeyboardInterrupt :
            exit()
        except Exception as ex:
            print("Upload failed(?) : " + str(ex))