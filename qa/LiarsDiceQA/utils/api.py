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

        def get_games_url(self, game_id=None):
            if game_id is not None:
                return self.get_url("/games/" + game_id)
            return self.get_url("/games")

        def games(self, payload=None, game_id=None):
            url = self.get_games_url(game_id=game_id)
            if payload is not None:
                return self.post(url, payload)
            return self.get(url)

        def get_claim_url(self, game_id):
            return self.get_url("/games/{id}/claim".format(id=game_id))

        def claim(self, game_id, payload, url_only=False):
            url = self.get_claim_url(game_id)
            if url_only:
                return url
            return self.post(url, payload)

        def get_challenge_url(self, game_id):
            return self.get_url("/games/{id}/challenge".format(id=game_id))

    instance = None

    def __new__(cls):
        if LiarsDiceApi.instance is None:
            LiarsDiceApi.instance = LiarsDiceApi.__LiarsDiceApi()
        return LiarsDiceApi.instance