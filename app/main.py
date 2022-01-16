import json, os, requests
from pprint import pprint

f = open('player.txt', 'r', encoding='UTF-8')
datalist = f.readlines()
Platform = datalist[0]
PlayerID = datalist[1]
url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + Platform + "/" + PlayerID + "/sessions"
f.close()

header = {"TRN-Api-Key":os.environ['112293c5-eb03-4ea1-a453-f0419f8e785d']}#環境変数から読み込むようにしてる
res = open(url, headers=header).json()
pprint(res)