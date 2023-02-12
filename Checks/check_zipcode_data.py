import pytest
import requests
import json

@pytest.mark.zipcode
def test_check_zipcode_data():
    res = requests.get('http://api.zippopotam.us/us/90210')
    res_text = res.json()
    print("Json Response from website: ",'\n',res_text)
    res_file = json_import()
    print("Json Response from the file: ",'\n',res_file)
    assert res_text['country'] == 'United States'
    assert res_text == res_file, 'failed'


def json_import():
    # Opening JSON file
    f = open('zipcode_90201.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    f.close()
    return data
