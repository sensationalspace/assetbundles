import unittest

class TestHelloWorld(unittest.TestCase):
    def test_output(self):
        output = "Hello World"
        self.assertEqual(output, "Hello World")

if __name__ == '__main__':
    unittest.main()
