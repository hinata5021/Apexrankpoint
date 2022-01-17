import json, os, requests, tkinter
from pprint import pprint



score_window = tkinter.Tk()
score_window.title("ランクポイント")
score_window.geometry("600x500")

#matchid.txt,player.txt,status.txtを読み込む
txtedit = open('app\status.txt', 'w', encoding='UTF-8')
f = open('app\player.txt', 'r', encoding='UTF-8')
match = open('app\matchid.txt', 'w', encoding='UTF-8')
confMatch = open('app\matchid.txt', 'w', encoding='UTF-8')


playerlist = f.read()
player = playerlist[0]
url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + player + "/sessions"
api_key = "112293c5-eb03-4ea1-a453-f0419f8e785d"
res = requests.get(url, "TRN-Api-Key=" + api_key)
ApexPS = json.loads(res.text)

rp = ApexPS["data"]["items"][0]["stats"]["rankScore"]["value"]
rpc = ApexPS["data"]["items"][0]["stats"]["rankScoreChange"]["value"]
pprint(rp)
pprint(rpc)

rankpoint = tkinter.Label(text=u'現在のランクポイント' + str(rp))
rankpoint.pack()
rankpointchange = tkinter.Label(text=u'ランクポイントの変化' + str(rpc))
rankpointchange.pack()


MatchID = ApexPS["data"]["items"][0]["matches"][0]["id"]#マッチIDを変数に代入
score = str(rp) + "," + str(rpc)




txtedit.write(score)
match.write(MatchID)


ReadCM = confMatch.read()


hukkin = 0
reflab = tkinter.Label(text=u'今日の腹筋回数' + hukkin)
reflab.pack()


def refresh():
    print("更新")
    pprint(rp)
    pprint(rpc)
    rankpoint['text'] ='現在のランクポイント' + str(rp)
    rankpointchange['text'] = 'ランクポイントの変化' + str(rpc)
    MatchID = ApexPS["data"]["items"][0]["matches"][0]["id"]
    match.write(MatchID)
    score = str(rp) + "," + str(rpc)
    txtedit.write(score)
    hukin = hukkin + rp
    huckin = hukin / 2
    reflab["text"] = '今日の腹筋回数' + huckin

def search():
    url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + player + "/sessions"
    api_key = "112293c5-eb03-4ea1-a453-f0419f8e785d"
    res = requests.get(url, "TRN-Api-Key=" + api_key)
    ApexPS = json.loads(res.text)
    MatchID = ApexPS["data"]["items"][0]["matches"][0]["id"]
    rp = ApexPS["data"]["items"][0]["stats"]["rankScore"]["value"]
    rpc = ApexPS["data"]["items"][0]["stats"]["rankScoreChange"]["value"]
    if ReadCM != MatchID:
        refresh()
        reflab['text'] = '更新しました。'

    else:
        reflab['text'] = 'すでに更新済みです。'


refb = tkinter.Button(text=u'更新', command=search)
refb.pack()








match.close()
txtedit.close()
f.close()
score_window.mainloop()



"""
matchid.txt,player.txt,status.txtを読み込む
ランクポイントとランクポイントの変化をメモ
マッチIDもメモ

マッチIDが更新されている場合
    マッチIDとスコアを書き換える
ランクポイント(txt)からランクポイント(変数)を引く
変数にいれる
その変数を表示




"""