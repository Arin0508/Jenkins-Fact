import unittest
from factorial import fact

class TestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(fact(0),1)

    def test_case2(self):
        self.assertEqual(fact(5),120)

    def test_case3(self):
        self.assertEqual(fact(10),3628800)  

if __name__ == '__main__':
    unittest.main()