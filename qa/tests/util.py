import requests
import unittest

class LiarsDiceApi(object):
    # static method to get the api object. In the real world, I would check for environment
    # vairables (set in Jenkins) to connect to the system under test

    class __LiarsDiceApi:
        def __init__(self):
            # In the real world, I might check for environment vairables
            # (set in Jenkins) to connect to the system under test
            self.host = "localhost"
            self.port = 8080
            self.base_url = "http://{host}:{port}".format(host=self.host, port=self.port)

        def _get(self, url):
            return requests.get(url)

        def _post(self, url, payload):
            headers = {'content-type': 'application/json'}
            return requests.post(url, payload, headers=headers)

        def games(self, payload=None):
            url = self.base_url + "/games"
            if payload is None:
                return self._get(url)
            else:
                return self._post(url, payload)

    instance = None

    def __new__(cls):
        if LiarsDiceApi.instance is None:
            LiarsDiceApi.instance = LiarsDiceApi.__LiarsDiceApi()
        return LiarsDiceApi.instance