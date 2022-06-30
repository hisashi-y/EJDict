import json
with open('ejdict_all.txt', 'r') as f:
    ejdict_rawdata = f.readlines()
# 英和辞典の生データを{'単語': '辞書のエントリー'}のdictにする
ejdict = {}
for line in ejdict_rawdata:
    line = line.split('\t')
    word = line[0].split(',')[0]
    meaning = line[1].split('\t')
    ejdict[word] = meaning

with open('ejdict_all.json', 'w') as f:
    json.dump(ejdict, f)