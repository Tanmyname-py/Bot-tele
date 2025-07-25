import json 

with open('session/ses.json','r') as f:
    data = json.load(f)

print(data)