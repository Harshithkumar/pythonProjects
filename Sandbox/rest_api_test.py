import requests
import json
import os

res = requests.get("https://api.stackexchange.com//2.3/answers/12?todate=1649030400&order=desc&max=1649116800&sort"
                   "=activity&site=stackoverflow")

#print(res.json()['items'])

print(res.status_code)



json_data = json.loads(res.text)
#print(str(json_data))
parse = {}
for i in json_data['items']:
    for j in i['owner']:
        parse[j] = parse.get(j)

print(parse)


# filename = "myfile.txt"
# file = open(filename, "w")
# json.dump(json_data, file)
# file.close()