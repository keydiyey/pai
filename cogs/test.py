import json
with open('./data/user_info.json', encoding = "utf8") as a:
       data = json.load(a)


if '845699992886050847' in data:
    
    print (data['845699992886050847'])
    
else: print (None)