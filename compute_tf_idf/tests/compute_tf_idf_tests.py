import unittest
from src.compute_tf_idf import App

class TestComputeTfIdfMethods(unittest.TestCase):


    def test_computeTfIdf_0(self):
        app0=App("./tests/documents", 10, "of", 3, "./tests/test0.log")
        app0.run_test()
        with open("./tests/test0.log") as f:
            self.assertEqual(f.readline(), "23.56700413903814 freedomspeech.txt\n")
            self.assertEqual(f.readline(), "18.714973875118524 sanmartin.txt\n")
            self.assertEqual(f.readline(), "17.328679513998633 ConstitutionUnitedStates.txt\n")

    def test_computeTfIdf_1(self):
        app1=App("./tests/documents", 10, "freedom", 3, "./tests/test1.log")
        app1.run_test()
        with open("./tests/test1.log") as f:
            self.assertEqual(f.readline(), "6.01986402162968 freedomspeech.txt\n")
            self.assertEqual(f.readline(), "2.4079456086518722 ThomasJefferson.txt\n")
            self.assertEqual(f.readline(), "0.0 stevejobs.txt\n")

    def test_computeTfIdf_2(self):
        app2=App("./tests/documents", 10, "freedom of", 3, "./tests/test2.log")
        app2.run_test()
        with open("./tests/test2.log") as f:
            self.assertEqual(f.readline(), "27.032740041837865 freedomspeech.txt\n")
            self.assertEqual(f.readline(), "18.714973875118524 sanmartin.txt\n")
            self.assertEqual(f.readline(), "18.021826694558577 ThomasJefferson.txt\n")

if __name__ == "__main__":
    unittest.main()