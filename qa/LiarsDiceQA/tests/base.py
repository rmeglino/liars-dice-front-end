import unittest
from collections import defaultdict
from utils import LiarsDiceApi



class BaseTest(unittest.TestCase):
    numPlayers = 4
    numDice = 5

    # set up a game to work with and record it's id for later use
    def setUp(self):
        self.api = LiarsDiceApi()
        payload = {"numPlayers": self.numPlayers, "numDice": self.numDice}
        resp = self.api.games(payload=payload)
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.game_id = resp_object['_id']

    # get count the number of faces and return the one with the highest count
    def _get_highest_number(self,nums):
        nmap = defaultdict(int)
        for num in nums:
            nmap[num] += 1
        top_count=0
        highest_number=0
        for key, value in nmap.items():
            if value > top_count:
                top_count = value
                highest_number = int(key)
        return highest_number, top_count
