import unittest
from collections import defaultdict
from utils import LiarsDiceApi
from base import BaseTest

class Test03Challenge(BaseTest):
    def testClaim0(self):
        # get the game
        game = self.api.games(game_id=self.game_id)

        #use the first player to make a claim
        player0_hand = game['playerHands'][0]
        moveFace, moveNumber = self._get_highest_number(player0_hand)
        payload = {"player": 0, "moveFace": moveFace, "moveNumber": moveNumber,
                   "claimFace": moveFace, "claimNumber": moveNumber + 1}
        resp = self.api.claim(self.game_id, payload)
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))

        #use the second player to challenge
        payload = {"player": 1}
        resp = self.api.challenge(self.game_id, payload)
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertTrue(isinstance(resp_object, bool))


