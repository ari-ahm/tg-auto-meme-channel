import requests
from redvid import Downloader
from os import path

subreddits = ["discordVideos", "WTF", "videomemes", "UnusualVideos", "shitposting", "HolUp"]

def getMedia(dct) :
    if ("data" in dct and "is_video" in dct["data"] and dct["data"]["is_video"]) :
        return dct["data"]["url"]
    return None

def getName(dct) :
    if ("data" in dct and "name" in dct["data"]) :
        return dct["data"]["name"]
    return None

def sortedByScore(dct) :
    return sorted(dct, key=lambda i : i["data"]["calc-score"], reverse=True)

def setScore(dct) :
    for i in dct :
        if (not "data" in i) :
            continue
        i["data"]["calc-score"] = i["data"]["score"] / i["data"]["subreddit_subscribers"] * 10 +\
                                    i["data"]["upvote_ratio"] * i["data"]["upvote_ratio"] * 1 +\
                                    i["data"]["num_comments"] / i["data"]["subreddit_subscribers"] * 3

def post(bot, conf) :
    opt = []
    for i in subreddits :
        opt += requests.get('https://oauth.reddit.com/r/{}/top'.format(i), headers=conf["reddit-header"], proxies=conf["proxy"]).json()["data"]["children"]
    setScore(opt)
    opt = sortedByScore(opt)
    dl = Downloader(max_q=True)
    for i in opt :
        print(i["data"]["calc-score"])
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
        
        # break