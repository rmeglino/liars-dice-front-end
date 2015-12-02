import unittest
import sys, inspect
import StringIO
from utils import HTMLTestRunner
import tests


class TestLiarsDice(unittest.TestCase):

    def runTest(self):
        testcases = []
        for name, obj in inspect.getmembers(tests):
            if inspect.isclass(obj):
                clsobj = eval('tests.' + name)
                testcases.append(unittest.defaultTestLoader.loadTestsFromTestCase(clsobj))

        # suite of TestCases
        self.suite = unittest.TestSuite()
        t = sorted(testcases)
        self.suite.addTests(testcases)

        # Invoke TestRunner
        buf = StringIO.StringIO()

        runner = HTMLTestRunner(
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