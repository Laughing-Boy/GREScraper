import csv
from random import choice,shuffle
from sys import argv
import requests
import vlc
start = argv[1] if len(argv) > 1 else 'a'
with open("repeat.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    arr = []
    selected_arr = []
    for row in reader:
        arr.append(dict(row))
csvfile.close()
for i in arr:
    if str(i['Word']).startswith(start):
        selected_arr.append(i)
#shuffle(selected_arr)
print(len(selected_arr))
for i in selected_arr:
    print( i['Word'])
    response = requests.get("https://googledictionaryapi.eu-gb.mybluemix.net/?define="+i['Word']+"&lang=en")
    data = response.json()
    try:
        audio_link = data[0]["pronunciation"]
        audio_clip = vlc.MediaPlayer(audio_link)
        audio_clip.play()
    except:
        pass
    input()
    print(str(i['Definition']).rstrip('\n').replace('\n', ' '))
    print(str(i['Example']).rstrip('\n'))
    for pos,info in data[0]["meaning"].items():
        #p(pos,info)
        for dic in info:
            for i,j in dic.items():
                if i == "synonyms":
                    print(i,":",*j[:5]) #p(i,":",*j)
##                elif i == "definition":
##                    p(pos,":",j)
##                else :
##                    p(i,":",j)
    input()

