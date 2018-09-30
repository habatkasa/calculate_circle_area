#Testmathfunctions

import unittest
import mathfunctions

class knownvalues(unittest.TestCase):
    #test area of a circle
    def test_areaCircle_for_10radius(self):
        result = mathfunctions.areaCircle(10)
        expected = 314.1592653589793
        self.assertEqual(expected,result)
    
    def test_areaCircle_for_2radius(self):
        result = mathfunctions.areaCircle(2)
        expected = 12.566370614359172
        self.assertEqual(expected,result)


if __name__ == '__main__':
    unittest.main()