import requests
import pytest

@pytest.mark.code
def test_status_code():
    res = requests.get('http://api.zippopotam.us/us/90210')
    print("Status Code: ",res.status_code)
    assert res.status_code == 200

@pytest.mark.code
def test_check_content_type():
    res = requests.get('http://api.zippopotam.us/us/90210')
    print("Content Type Value: ",res.headers["Content-Type"])
    assert res.headers["Content-Type"] == "application/json"

@pytest.mark.code
def test_country_value():
    res = requests.get('http://api.zippopotam.us/us/90210')
    res_text = res.json()
    print("Country value: ", res_text['country'])
    assert res_text['country'] == 'United States'

@pytest.mark.sample
def test_print_json_response():
    res = requests.get('http://api.zippopotam.us/us/90210')
    res_text = res.json()
    print("Json Response",res_text)

@pytest.mark.sample
def test_json_array():
    res = requests.get('http://api.zippopotam.us/us/90210')
    res_text = res.json()
    array_places = res_text['places']
    arr_resp = array_places[0]
    print(arr_resp)
    placename = array_places[0]['place name']
    logitude = array_places[0]['longitude']
    print("logitude = ", logitude)
    print("Placename = ", placename)