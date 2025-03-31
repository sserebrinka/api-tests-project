import requests
from utils.logger import Logger

class HttpMethods:
    """Список HTTP методов"""

    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @classmethod
    def get(cls, url):
        Logger.add_request(url, method='GET')
        result = requests.get(url=url, headers=cls.headers, cookies=cls.cookie)
        Logger.add_response(result)
        return result

    @classmethod
    def post(cls, url, body):
        Logger.add_request(url, method='POST')
        result = requests.post(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
        Logger.add_response(result)
        return result

    @classmethod
    def put(cls, url, body):
        Logger.add_request(url, method='PUT')
        result = requests.put(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
        Logger.add_response(result)
        return result

    @classmethod
    def delete(cls, url, body):
        Logger.add_request(url, method='DELETE')
        result = requests.delete(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
        Logger.add_response(result)
        return result