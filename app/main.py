import json, os, requests
from pprint import pprint

f = open('player.txt', 'r', encoding='UTF-8')
datalist = f.readlines()
Platform = datalist[0]
PlayerIS = datalist[1]
url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + Platform + "/" + PlayerID + "/sessions"
f.close()

header = {"TRN-Api-Key":os.environ['TRN_API_KEY']}#環境変数から読み込むようにしてる
res = open(url, headers=header).json()
pprint(res)