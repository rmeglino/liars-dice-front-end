import unittest
from collections import defaultdict
from utils import LiarsDiceApi
from base import BaseTest


class Test03Challenge(BaseTest):

    def setUp(self):
        super(Test03Challenge, self).setUp()
        self.game = self.api.games(game_id=self.game_id).json()
        player0_hand = self.game['playerHands'][0]
        moveFace, moveNumber = self._get_highest_number(player0_hand)
        payload = {"player": 0, "moveFace": moveFace, "moveNumber": moveNumber,
                   "claimFace": moveFace, "claimNumber": moveNumber + 1}
        resp = self.api.claim(self.game_id, payload)
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))

    def test0_missing_gameId(self):
        # given
        # gameId = missing
        # player = defined

        payload = {"player": 1}
        game_id = ""

        # when
        url = self.api.get_challenge_url(game_id)
        resp = self.api.post(url, payload)

        # then should fail
        self.assertEqual(resp.status_code, 404)

    def test1_missing_player(self):
        # given
        # gameId = defined
        # player = missing

        payload = {}
        game_id = self.game_id

        # when
        url = self.api.get_challenge_url(game_id)
        resp = self.api.post(url, payload)

        # then should fail
        self.assertEqual(resp.status_code, 404)

    def test2_all_defined(self):
        # given
        # gameId = defined
        # player = defined

        payload = {"player": 1}
        game_id = self.game_id

        # when
        url = self.api.get_challenge_url(game_id)
        resp = self.api.post(url, payload)
        resp_object = resp.json()

        # then should pass
        self.assertTrue(isinstance(resp_object, bool))



