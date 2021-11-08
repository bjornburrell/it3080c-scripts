import requests
import json

r = requests.get('http://localhost:3000')
dataList = r.json()

index = 0
while index < len(dataList):
    for key in dataList[index]:
        print(dataList[index][key])
        
    index += 1

