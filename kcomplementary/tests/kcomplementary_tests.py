import unittest
from src.kcomplementary import kcomplementary

class TestKcomplementaryMethods(unittest.TestCase):

    def test_kcomplementary_limite_cases(self):
        self.assertEqual(kcomplementary([],1),[])
        self.assertEqual(kcomplementary([2],4),[0])

    def test_kcomplementary_numbers(self):
        self.assertEqual(kcomplementary([1,2,3,4],5),[3, 2, 1, 0])
        self.assertEqual(kcomplementary([2,0,3,5],5),[2, 3, 0, 1])
        self.assertEqual(kcomplementary([-1,6,3,7,0],6),[3, 4, 2, 0, 1])
        self.assertEqual(kcomplementary([1.5,0.5,(-0.5),2.5],2),[1, 0, 3, 2])

    def test_nokcomplementary_numbers(self):
        self.assertEqual(kcomplementary([0,6,3,7,1],6),[1, 0, 2, None, None])
        self.assertEqual(kcomplementary([1.5,0.5,(-0.2),2.3],2),[1, 0, None, None])        


if __name__ == "__main__":
	unittest.main()