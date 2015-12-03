import unittest
from utils import LiarsDiceApi

api = LiarsDiceApi()
numPlayers = 4
numDice = 5

class Test01Games(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        resp = api.games()
        resp_object = resp.json()
        Test01Games.numExistingGames = len(resp_object)

    # numPlayers defined
    # numDice missing
    # should fail
    def test0_numDice_missing(self):
        payload = {'numPlayers': numPlayers }
        url = api.get_url("/games")
        resp = api.post(url, payload)
        self.assertEqual(resp.status_code, 200)
        resp_obj = resp.json()
        self.assertEqual(resp_obj.get("error", None), "numPlayers and numDice is required")

    # numPlayers missing
    # numDice defined
    # should fail
    def test1_numPlayers_missing(self):
        payload = {'numDIce': numDice }
        url = api.get_url("/games")
        resp = api.post(url, payload)
        self.assertEqual(resp.status_code, 200)
        resp_obj = resp.json()
        self.assertEqual(resp_obj.get("error", None), "numPlayers and numDice is required")

    # empty payload
    # should fail
    def test2_empty_payload(self):
        payload = {}
        url = api.get_url("/games")
        resp = api.post(url, payload)
        self.assertEqual(resp.status_code, 200)
        resp_obj = resp.json()
        self.assertEqual(resp_obj.get("error", None), "numPlayers and numDice is required")

    # numPlayers defined
    # numDice defined
    # should pass
    def test3_payload_defined(self):
        payload = {"numPlayers": numPlayers, "numDice": numDice}
        resp = api.games(payload=payload)
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertIsNotNone(resp_object.get("_id", None))
        Test01Games.game_id = resp_object['_id']
        self.assertEqual(resp_object.get("numPlayers", None), numPlayers)
        self.assertEqual(resp_object.get("numDice", None), numDice)
        self.assertIsNotNone(resp_object.get("playerHands", None))
        self.assertEqual(len(resp_object['playerHands']), numPlayers)
        for hand in resp_object.get("playerHands", None):
            self.assertEqual(len(hand), numDice)

    # get multiple games
    def test4_get_multiple_games(self):
        url = api.get_url("/games")
        resp = api.get(url)
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsInstance(resp_object, list)
        self.assertEqual(len(resp_object), self.numExistingGames + 1)

    # get single game
    def test5_get_single_game(self):
        url = api.get_url("/games/" + Test01Games.game_id)
        resp = api.get(url)
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsInstance(resp_object, dict)
