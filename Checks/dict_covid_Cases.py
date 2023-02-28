import json
import requests
import pandas

URL = 'https://api.covid19api.com/summary'

response_data = requests.get(URL)
parsed_data = json.loads(response_data.text)
print(parsed_data)

global_confirmed_Cases = int(parsed_data['Global']['TotalConfirmed'])
print('Global_Confirmed_Cases = ', global_confirmed_Cases)

list_of_countries = []
cn_total_confirmedcases = 0
for cn_info in parsed_data['Countries']:
    each_cn = cn_info['Country']
    total_confirmed_Cases = cn_info['TotalConfirmed']
    list_of_countries.append([each_cn, total_confirmed_Cases])
    cn_total_confirmedcases += int(total_confirmed_Cases)
print('list_of_countries = ', list_of_countries)
print('cn_total_confirmed_cases =', cn_total_confirmedcases)

data_frame = pandas.DataFrame(data=list_of_countries, columns=['each_cn','total_confirmed_Cases'])

print(data_frame.head(10))

assert global_confirmed_Cases == cn_total_confirmedcases, " Total cofirmed cases not matached"




