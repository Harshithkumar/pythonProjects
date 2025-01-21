import requests
import json

class Base_api_methods():

    base_url = "http://authservice-staging.tpa1.tivo.com"
    port = "50240"
    headers = {"content-type":"application/json",
               "schemaversion": "40"
               }

    def post_request(self, url, payload, headers):
        response = requests.post(url=url, data=payload, headers=headers)
        return self.__get_responses(response)

    def get_request(self, url, headers):
        response = requests.get(url=url, headers=headers)
        return self.__get_responses(response)

    def put_request(self, url, payload, headers):
        response = requests.put(url=url, data=payload, headers=headers)
        return self.__get_responses(response)

    def delete_request(self, url, headers):
        response = requests.delete(url=url, data=None, headers=headers)
        return self.__get_responses(response)