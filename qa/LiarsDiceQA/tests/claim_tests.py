import unittest
from collections import defaultdict
from utils import LiarsDiceApi
from base import BaseTest


class Test02Claims(BaseTest):

    def testClaim0(self):
        # get the game
        game = self.api.games(game_id=self.game_id)

        #use the first player to make a claim
        player0_hand = game['playerHands'][0]
        moveFace, moveNumber = self._get_highest_number(player0_hand)
        payload = {"player": 0, "moveFace": moveFace, "moveNumber": moveNumber,
                   "claimFace": moveFace, "claimNumber": moveNumber + 10}
        resp = self.api.claim(self.game_id, payload)

        # make sure the claim went though
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(len(resp_object['document']['board']), moveNumber)
        hand = resp_object['document']['playerHands'][0]
        self.assertEqual(len(hand), self.numDice - moveNumber)

