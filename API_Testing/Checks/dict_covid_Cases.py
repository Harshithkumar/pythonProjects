import json
import requests
import pandas
import pytest


class Test_matchConfirmedCases:
    URL = 'https://api.covid19api.com/summary'

    @pytest.mark.GetURL
    def test_getResponse(self):
        response_data = requests.get(self.URL)
        parsed_data = json.loads(response_data.text)
        print(parsed_data)
        return parsed_data

    def test_getGlobalConfirmedCases(self):
        global_parsed_data = Test_matchConfirmedCases.test_getResponse(self)
        global_confirmed_Cases = int(global_parsed_data['Global']['TotalConfirmed'])
        print('Global_Confirmed_Cases = ', global_confirmed_Cases)
        return global_confirmed_Cases

    def test_Calculate_confirmed_cases(self):
        list_of_countries = []
        cn_total_confirmedcases = 0
        summary_data = Test_matchConfirmedCases.test_getResponse(self)
        for cn_info in summary_data['Countries']:
            each_cn = cn_info['Country']
            total_confirmed_Cases = cn_info['TotalConfirmed']
            list_of_countries.append([each_cn, total_confirmed_Cases])
            cn_total_confirmedcases += int(total_confirmed_Cases)
            # print('list_of_countries = ', list_of_countries)
        print('cn_total_confirmed_cases =', cn_total_confirmedcases)
        return list_of_countries, cn_total_confirmedcases

    def test_make_Table(self):
        list_of_countries, cn_total_confirmedcases = Test_matchConfirmedCases.test_Calculate_confirmed_cases(self)
        global_confirmed_Cases = Test_matchConfirmedCases.test_getGlobalConfirmedCases(self)
        data_frame = pandas.DataFrame(data=list_of_countries, columns=['each_cn', 'total_confirmed_Cases'])
        print(data_frame.head(10))
        assert global_confirmed_Cases == cn_total_confirmedcases, " Total cofirmed cases not matached"
