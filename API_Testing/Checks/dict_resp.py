import json
import requests
import pandas

URL = 'https://api.covid19api.com/countries'

response_data = requests.get(URL)
parsed_data = json.loads(response_data.text)
print(parsed_data)

#global_confirmed_Cases = parsed_data['Global']['TotalConfirmed']
#print('Global_Confirmed_Cases = ', global_confirmed_Cases)

list_of_countries = []
for cn_info in parsed_data:
    each_cn = cn_info['Country']
    each_cn_ISO2 = cn_info['ISO2']
    list_of_countries.append([each_cn, each_cn_ISO2])
print('list_of_countries = ', list_of_countries)

data_frame = pandas.DataFrame(data=list_of_countries, columns=['each_cn','each_cn_ISO2'])

print(data_frame.head(10))




