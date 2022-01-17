from ast import Str
import json, os, requests, tkinter, time, threading
from pprint import pprint



score_window = tkinter.Tk()
score_window.title("ランクポイント")
score_window.geometry("600x500")


txtedit = open('app\status.txt', 'w', encoding='UTF-8')
f = open('app\player.txt', 'r', encoding='UTF-8')
match = open('app\matchid.txt', 'w', encoding='UTF-8')
confMatch = open('app\matchid.txt', 'r', encoding='UTF-8')


playerlist = f.readlines()
player = playerlist[0]
url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + player + "/sessions"
api_key = "112293c5-eb03-4ea1-a453-f0419f8e785d" #トラッカーのAPIキーです
res = requests.get(url, "TRN-Api-Key=" + api_key)
ApexPS = json.loads(res.text)
rp = ApexPS["data"]["items"][0]["stats"]["rankScore"]["value"]
rpc = ApexPS["data"]["items"][0]["stats"]["rankScoreChange"]["value"]
pprint(rp)
pprint(rpc)

MatchID = ApexPS["data"]["items"][0]["matches"][0]["id"]
match.write(MatchID)


rankpoint = tkinter.Label(text=u'現在のランクポイント' + str(rp))
rankpoint.pack()
rankpointchange = tkinter.Label(text=u'ランクポイントの変化' + str(rpc))
rankpointchange.pack()
score = str(rp) + "," + str(rpc)
txtedit.writelines(score)

ReadCM = confMatch.read()

def thread1():
    if ReadCM != MatchID:

        while True:
            time.sleep(5)
            url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + player + "/sessions"
            api_key = "112293c5-eb03-4ea1-a453-f0419f8e785d" #トラッカーのAPIキーです。いじらないでください。
            res = requests.get(url, "TRN-Api-Key=" + api_key)
            ApexPS = json.loads(res.text)
            rp = ApexPS["data"]["items"][0]["stats"]["rankScore"]["value"]
            rpc = ApexPS["data"]["items"][0]["stats"]["rankScoreChange"]["value"]
            print("更新")
            pprint(rp)
            pprint(rpc)
            rankpoint['text'] ='現在のランクポイント' + str(rp)
            rankpointchange['text'] = 'ランクポイントの変化' + str(rpc)
            match.write(MatchID)

t1 = threading.Thread(target = thread1)
t1.start()
t1.join()











match.close()
txtedit.close()
f.close()
score_window.mainloop()