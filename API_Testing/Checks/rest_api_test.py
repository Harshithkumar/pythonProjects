import webbrowser

import requests
import json
import os

res = requests.get("https://api.stackexchange.com//2.3/answers/12?todate=1649030400&order=desc&max=1649116800&sort"
                   "=activity&site=stackoverflow")

#print(res.json()['items'])

print(res.status_code, res.request, res.links, res.raw, res.is_redirect, res.history)


json_data_0 = res.json()          # this and below line are same
json_data = json.loads(res.text)
print('type: ', type(json_data))
print("response", res.text)
print('quota_max = ', json_data['quota_max'])
parse = {}
for i in json_data['items']:
    parse = i['owner']
print('under Owner', parse)




link = parse.get('link')
display_name = parse.get('display_name')
print('display_name = ',display_name)
#webbrowser.open(link)

parse_2 = {}
for i in json_data['items']:
    parse_2 = i
print('under items', parse_2)

content_license = parse_2.get('content_license')
print('content_license =', content_license)
