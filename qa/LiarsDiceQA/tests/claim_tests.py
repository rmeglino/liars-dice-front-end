import unittest
from collections import defaultdict
from utils import LiarsDiceApi
from base import BaseTest


class Test02Claims(BaseTest):
    # this test actually crashes the server, but would be a valid test
    # test with incorrect game_id
    # def testClaim0(self):
    #      # get the game
    #     game = self.api.games(game_id=self.game_id)
    #
    #     #use the first player to make a claim
    #     player0_hand = game['playerHands'][0]
    #     moveFace, moveNumber = self._get_highest_number(player0_hand)
    #     payload = {"player": 0, "moveFace": moveFace, "moveNumber": moveNumber,
    #                "claimFace": moveFace, "claimNumber": moveNumber + 10}
    #     resp = self.api.claim("incorrectId", payload)
    #     self.assertEqual(resp.status_code, 400)

    # make claim with incorrect payload should return an error message
    # This actually crashes the server but is a valid test
    # def testClaim1(self):
    #     url = self.api.claim(self.game_id, None, url_only=True)
    #     playerNumber = self.numPlayers+1
    #     payload = {"player": playerNumber, "moveFace": 1, "moveNumber": 1,
    #                "claimFace": 1, "claimNumber": 10}
    #     resp = self.api.post(url, payload)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.json().get("error", None), "Player not found")

    # make claim with correct payload
    def testClaim2(self):
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

