import unittest
from collections import defaultdict
from utils import LiarsDiceApi
from base import BaseTest

class Test02Claims(BaseTest):

    def _get_face_not_in(self, hand):
        for x in range(1,7):
            if x not in hand:
                return x

    def setUp(self):
        super(Test02Claims, self).setUp()
        self.game = self.api.games(game_id=self.game_id).json()
        self.player0_hand = self.game['playerHands'][0]
        self.moveFace, self.moveNumber = self._get_highest_number(self.player0_hand)

    def test0_all_defined(self):
        # given
        # gameId = defined
        # player = defined
        # moveNumber = numberInHand
        # moveFace = presentInHand
        # claimNumber = defined
        # claimFace = 1-6

        game_id = self.game_id
        payload = {"player": 0, "moveFace": self.moveFace, "moveNumber": self.moveNumber,
                   "claimFace": self.moveFace, "claimNumber": self.moveNumber + 10}

        # when
        resp = self.api.claim(game_id, payload)

        # then should pass
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(len(resp_object['document']['board']), self.moveNumber)
        hand = resp_object['document']['playerHands'][0]
        self.assertEqual(len(hand), self.numDice - self.moveNumber)

    def test1_all_defined(self):
        # given
        # gameId = defined
        # player = defined
        # moveNumber = numberInHand
        # moveFace = presentInHand
        # claimNumber = defined
        # claimFace = 1-6

        game_id = self.game_id
        payload = {"player": 0, "moveFace": self.moveFace, "moveNumber": self.moveNumber,
                   "claimFace": self.moveFace, "claimNumber": self.moveNumber + 10}

        # when
        resp = self.api.claim(game_id, payload)

        # then should pass
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(len(resp_object['document']['board']), self.moveNumber)
        hand = resp_object['document']['playerHands'][0]
        self.assertEqual(len(hand), self.numDice - self.moveNumber)


    def test2_missing_gameId(self):
        # given
        # gameId = missing
        # player = defined
        # moveNumber = numberInHand
        # moveFace = presentInHand
        # claimNumber = defined
        # claimFace = 1-6

        game_id = ""
        payload = {"player": 0, "moveFace": self.moveFace, "moveNumber": self.moveNumber,
                   "claimFace": self.moveFace, "claimNumber": self.moveNumber + 10}
        # when
        resp = self.api.claim(game_id, payload)

        # then should fail
        self.assertEqual(resp.status_code, 404)

    @unittest.skip("this test crashes the system - a defect report should be written up on this")
    def test3_missing_player(self):
        # given
        # gameId = defined
        # player = missing
        # moveNumber = numberInHand
        # moveFace = presentInHand
        # claimNumber = defined
        # claimFace = 1-6

        game_id = self.game_id
        payload = {"moveFace": self.moveFace, "moveNumber": self.moveNumber,
                   "claimFace": self.moveFace, "claimNumber": self.moveNumber + 10}
        # when
        resp = self.api.claim(game_id, payload)

        # then should fail
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertEqual(resp_object.get("error", None), "missing required field")


    def test4_missing_moveNumber(self):
        # given
        # gameId = defined
        # player = defined
        # moveNumber = missing
        # moveFace = presentInHand
        # claimNumber = defined
        # claimFace = 1-6

        game_id = self.game_id
        payload = {"player": 0, "moveFace": self.moveFace,
                   "claimFace": self.moveFace, "claimNumber": self.moveNumber + 10}
        # when
        resp = self.api.claim(game_id, payload)

        # then should pass with no change or fail
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(len(resp_object['document']['board']), 0)
        hand = resp_object['document']['playerHands'][0]
        self.assertEqual(len(hand), self.numDice)


    def test5_moveNumber_0(self):
        # given
        # gameId = defined
        # player = defined
        # moveNumber = 0
        # moveFace = presentInHand
        # claimNumber = defined
        # claimFace = 1-6

        game_id = self.game_id
        payload = {"player": 0, "moveFace": self.moveFace, "moveNumber": 0,
                   "claimFace": self.moveFace, "claimNumber": self.moveNumber + 10}

        # when
        resp = self.api.claim(game_id, payload)

        # then should pass with no change or fail
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(len(resp_object['document']['board']), 0)
        hand = resp_object['document']['playerHands'][0]
        self.assertEqual(len(hand), self.numDice)

    def test6_moveNumber_100(self):
        # given
        # gameId = defined
        # player = defined
        # moveNumber = 100
        # moveFace = presentInHand
        # claimNumber = defined
        # claimFace = 1-6

        game_id = self.game_id
        payload = {"player": 0, "moveFace": self.moveFace, "moveNumber": 100,
                   "claimFace": self.moveFace, "claimNumber": self.moveNumber + 10}

        # when
        resp = self.api.claim(game_id, payload)

        # then should  pass with no change
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(len(resp_object['document']['board']), 0)
        hand = resp_object['document']['playerHands'][0]
        self.assertEqual(len(hand), self.numDice)


    def test7_missing_moveFace(self):
        # given
        # gameId = defined
        # player = defined
        # moveNumber = numberInHand
        # moveFace = missing
        # claimNumber = defined
        # claimFace = 1-6

        game_id = self.game_id
        payload = {"player": 0, "moveNumber": self.moveNumber,
                   "claimFace": self.moveFace, "claimNumber": self.moveNumber + 10}

        # when
        resp = self.api.claim(game_id, payload)

        # then should  pass with no change
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(len(resp_object['document']['board']), 0)
        hand = resp_object['document']['playerHands'][0]
        self.assertEqual(len(hand), self.numDice)

    def test8_missing_claimNumber(self):
        # given
        # gameId = defined
        # player = defined
        # moveNumber = numberInHand
        # moveFace = presentInHand
        # claimNumber = missing
        # claimFace = 1-6

        game_id = self.game_id
        payload = {"player": 0, "moveFace": self.moveFace, "moveNumber": self.moveNumber,
                   "claimFace": self.moveFace}

        # when
        resp = self.api.claim(game_id, payload)

        # then should pass with no change or fail
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(len(resp_object['document']['board']), 0)
        hand = resp_object['document']['playerHands'][0]
        self.assertEqual(len(hand), self.numDice)

    def test9_missing_claimFace(self):
        # given
        # gameId = defined
        # player = defined
        # moveNumber = numberInHand
        # moveFace = presentInHand
        # claimNumber = defined
        # claimFace = missing 
        
        game_id = self.game_id
        payload = {"player": 0, "moveFace": self.moveFace, 
                   "moveNumber": self.moveNumber,"claimNumber": self.moveNumber + 10}

        # when
        resp = self.api.claim(game_id, payload)

        # then should pass with no change or fail
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(len(resp_object['document']['board']), 0)
        hand = resp_object['document']['playerHands'][0]
        self.assertEqual(len(hand), self.numDice)


    def test10_moveFace_not_in_hand(self):
        # given
        # gameId = defined
        # player = defined
        # moveNumber = numberInHand
        # moveFace = notInHand
        # claimNumber = defined
        # claimFace = 1-6

        game_id = self.game_id
        moveFace = self._get_face_not_in(self.player0_hand)
        payload = {"player": 0, "moveFace": moveFace, "moveNumber": self.moveNumber,
                   "claimFace": self.moveFace, "claimNumber": self.moveNumber + 10}

        # when
        resp = self.api.claim(game_id, payload)

        # then should pass with no change or fail
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(len(resp_object['document']['board']), 0)
        hand = resp_object['document']['playerHands'][0]
        self.assertEqual(len(hand), self.numDice)

    def test11_claimFace_greater_than_6(self):
        # given
        # gameId = defined
        # player = defined
        # moveNumber = numberInHand
        # moveFace = presentInHand
        # claimNumber = defined
        # claimFace = greaterThan_6

        game_id = self.game_id
        payload = {"player": 0, "moveFace": self.moveFace, "moveNumber": self.moveNumber,
                   "claimFace": 8, "claimNumber": self.moveNumber + 10}

        # when
        resp = self.api.claim(game_id, payload)

        # then should pass with no change or fail
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertIsNone(resp_object.get("error", None))
        self.assertEqual(len(resp_object['document']['board']), 0)
        hand = resp_object['document']['playerHands'][0]
        self.assertEqual(len(hand), self.numDice)