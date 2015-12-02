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

    # try to create a game without payload
    def test0(self):
        payload = {}
        url = api.get_url("/games")
        resp = api.post(url, payload)
        self.assertEqual(resp.status_code, 200)
        resp_obj = resp.json()
        self.assertEqual(resp_obj.get("error", None), "numPlayers and numDice is required")

    # Next, create a game for real
    def test1(self):
        payload = {"numPlayers": numPlayers, "numDice": numDice}
        resp = api.games(payload=payload)
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(resp_object.get("numPlayers", None), numPlayers)
        self.assertEqual(resp_object.get("numDice", None), numDice)
        self.assertIsNotNone(resp_object.get("playerHands", None))
        self.assertEqual(len(resp_object['playerHands']), numPlayers)
        for hand in resp_object.get("playerHands", None):
            self.assertEqual(len(hand), numDice)

    # Now, test that the game exists
    def test2(self):
        resp = api.games()
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertEqual(len(resp_object), self.numExistingGames + 1)
