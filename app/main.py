import json, requests, tkinter
from pprint import pprint



score_window = tkinter.Tk()
score_window.title("ランクポイント")
score_window.geometry("600x500")

#player.txt,APIkeyを読み込む
f = open('player.txt', 'r', encoding='UTF-8')
apitxt = open('mapi.txt', 'r', encoding='UTF-8')
playerr = f.readlines()
apikyr = apitxt.readlines()
player = playerr[0]
apiky = apikyr[0]
url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + str(player)
res = requests.get(url, "TRN-Api-Key=" + str(apiky))
apex = json.loads(res.text)
beforejson = apex["data"]["segments"][0]["stats"]["rankScore"]["value"]
rankpoint = tkinter.Label(text=u'現在のランクポイント' + str(beforejson))
rankpoint.pack()
hukkin = 0
reflab = tkinter.Label(text=u'今日の腹筋回数' + str(hukkin))
reflab.pack()
refresh = tkinter.Label(text=u'')
refresh.pack()

def ifjson():
    global beforejson
    f = open('player.txt', 'r', encoding='UTF-8')
    apitxt = open('mapi.txt', 'r', encoding='UTF-8')
    playerr = f.readlines()
    apikyr = apitxt.readlines()
    player = playerr[0]
    apiky = apikyr[0]
    url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + str(player)
    res = requests.get(url, "TRN-Api-Key=" + str(apiky))
    ApexPS = json.loads(res.text)
    afterjson = ApexPS["data"]["segments"][0]["stats"]["rankScore"]["value"]
    if beforejson != afterjson:
        rankpoint['text'] ='現在のランクポイント' + str(afterjson)
        hukin = beforejson - afterjson
        x = hukin * -1
        huckin = x / 2
        reflab["text"] = '今日の筋トレ回数: ' + str(huckin)
        refresh['text'] = '更新しました。'
        apitxt.close()
        f.close()
        beforejson = afterjson
    else:
        refresh['text'] = 'マッチの処理がまだできていません。少し待ってから更新してください。'


        

rebutton = tkinter.Button(text=u'更新', command=ifjson)
rebutton.pack()


apitxt.close()
f.close()




score_window.mainloop()