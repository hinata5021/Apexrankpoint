import json, os, requests, tkinter
from pprint import pprint



score_window = tkinter.Tk()
score_window.title("ランクポイント")
score_window.geometry("600x500")

#matchid.txt,player.txt,status.txtを読み込む
txtedit = open('app\status.txt', 'w', encoding='UTF-8')
f = open('app\player.txt', 'r', encoding='UTF-8')
match = open('app\matchid.txt', 'w', encoding='UTF-8')
confMatch = open('app\matchid.txt', 'r+', encoding='UTF-8')
apitxt = open('app\mapi.txt', 'r', encoding='UTF-8')


playerr = f.readlines()
apikyr = apitxt.readlines()
player = playerr[0]
apiky = apikyr[0]
url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + player + "/sessions"
res = requests.get(url, "TRN-Api-Key=" + apiky)
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


ReadCM = confMatch.read()#マッチIDをロード


hukkin = 0
reflab = tkinter.Label(text=u'今日の腹筋回数' + str(hukkin))
reflab.pack()

refresh = tkinter.Label(text=u'')
refresh.pack()

def search():
    txtedit = open('app\status.txt', 'w', encoding='UTF-8')
    f = open('app\player.txt', 'r', encoding='UTF-8')
    match = open('app\matchid.txt', 'w', encoding='UTF-8')
    confMatch = open('app\matchid.txt', 'r+', encoding='UTF-8')
    apitxt = open('app\mapi.txt', 'r', encoding='UTF-8')
    playerr = f.readlines()
    apikyr = apitxt.readlines()
    player = playerr[0]
    apiky = apikyr[0]
    url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + player + "/sessions"
    res = requests.get(url, "TRN-Api-Key=" + apiky)
    ApexPS = json.loads(res.text)
    MatchID = ApexPS["data"]["items"][0]["matches"][0]["id"]
    rp2 = ApexPS["data"]["items"][0]["stats"]["rankScore"]["value"]
    rpc2 = ApexPS["data"]["items"][0]["stats"]["rankScoreChange"]["value"]

    if ReadCM != MatchID:
        print("更新")
        rankpoint['text'] ='現在のランクポイント' + str(rp2)
        rankpointchange['text'] = 'ランクポイントの変化' + str(rpc2)
        match.write(MatchID)
        score = str(rp2) + "," + str(rpc2)
        txtedit.write(score)
        hukin = rp2 - rp
        huckin = hukin / 2
        reflab["text"] = '今日の筋トレ回数: ' + str(huckin)
        pprint(rp)
        pprint(rpc)
        refresh['text'] = '更新しました。'
        confMatch.close()
        apitxt.close()
        match.close()
        txtedit.close()
        f.close()

    else:
        refresh['text'] = 'すでに更新済みです。'


refb = tkinter.Button(text=u'更新', command=search)
refb.pack()


confMatch.close()
apitxt.close()
match.close()
txtedit.close()
f.close()




score_window.mainloop()