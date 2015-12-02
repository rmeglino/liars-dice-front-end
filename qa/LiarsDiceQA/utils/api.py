import requests
import json

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

        def get(self, url):
            return requests.get(url)

        def post(self, url, payload):
            headers = {'content-type': 'application/json'}
            return requests.post(url, json.dumps(payload), headers=headers)

        def get_url(self,path):
            return self.base_url + path

        def games(self, payload=None, game_id=None):
            url = self.get_url("/games")
            if payload is not None:
                return self.post(url, payload)
            if payload is None and game_id is None:
                return self.get(url)
            else:
                resp_object = self.get(url).json()
                for game in resp_object:
                    if game['_id'] == game_id:
                        return game
                return None

        def claim(self, game_id, payload, url_only=False):
            url = self.get_url("/games/{id}/claim".format(id=game_id))
            if url_only:
                return url
            return self.post(url, payload)

        def challenge(self, game_id, payload, url_only=False):
            url = self.get_url("/games/{id}/challenge".format(id=game_id))
            if url_only:
                return url
            return self.post(url, payload)

    instance = None

    def __new__(cls):
        if LiarsDiceApi.instance is None:
            LiarsDiceApi.instance = LiarsDiceApi.__LiarsDiceApi()
        return LiarsDiceApi.instance