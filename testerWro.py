import unittest
from factorial import fact

class TestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(fact(-1),0)

    def test_case2(self):
        self.assertEqual(fact(-10),0)


if __name__ == '__main__':
    unittest.main()