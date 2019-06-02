import csv
from random import choice,shuffle


start = "v"
with open("magoosh.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    arr = []
    selected_arr = []
    for row in reader:
        arr.append(dict(row))
csvfile.close()
for i in arr:
    if str(i['Word']).startswith(start):
        selected_arr.append(i)
shuffle(selected_arr)
print(len(selected_arr))
for i in selected_arr:
    print( i['Word'])
    input()
    print(str(i['Definition']).rstrip('\n').replace('\n', ' '))
    print(str(i['Example']).rstrip('\n'))

