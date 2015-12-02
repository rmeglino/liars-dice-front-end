import StringIO
import json
import unittest

import HTMLTestRunner
from util import LiarsDiceApi

api = LiarsDiceApi()
numPlayers = 4
numDice = 5

class TestGames(unittest.TestCase):
    # First test that games returns an empty list
    def test0(self):
        resp = api.games()
        self.assertEqual(resp.status_code, 200)
        resp_object = resp.json()
        self.assertEqual(len(resp_object), 0)

    # Next, create a game
    def test1(self):
        payload = {"numPlayers": numPlayers, "numDice": numDice}
        resp = api.games(payload=json.dumps(payload))
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
        self.assertEqual(len(resp_object), 1)
        game = resp_object[0]
        self.assertIsNone(game.get("error", None))
        self.assertEqual(game.get("numPlayers", None), numPlayers)
        self.assertEqual(game.get("numDice", None), numDice)
        self.assertIsNotNone(game.get("playerHands", None))
        self.assertEqual(len(game['playerHands']), numPlayers)
        for hand in game.get("playerHands", None):
            self.assertEqual(len(hand), numDice)


class TestLiarsDice(unittest.TestCase):

    def runTest(self):

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGames),
            ])

        # Invoke TestRunner
        buf = StringIO.StringIO()

        runner = HTMLTestRunner.HTMLTestRunner(
            stream=buf,
            title='Liars Dice Tests',
            description='This test suite exercises the Liars Dice node.js endpoints.'
        )

        runner.run(self.suite)
        byte_output = buf.getvalue()
        output = byte_output.decode('utf-8')
        f = file("results.html", 'w')
        f.write(output)
        f.flush()
        f.close()

if __name__ == "__main__":
    argv=['tests.py', 'TestLiarsDice']
    unittest.main(argv=argv)