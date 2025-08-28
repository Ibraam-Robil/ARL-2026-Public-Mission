import unittest
from Question import fuse_readings  

class TestSensorFusion(unittest.TestCase):

    def test_all_agree(self):
        s1 = [100, 200, 300]
        s2 = [100, 200, 300]
        s3 = [100, 200, 300]
        expected = [100, 200, 300]
        self.assertEqual(fuse_readings(s1, s2, s3), expected)

    def test_majority_agree(self):
        s1 = [80, 70, 60, 90]
        s2 = [80, 72, 60, 91]
        s3 = [82, 70, 59, 90]
        expected = [80, 70, 60, 90]
        self.assertEqual(fuse_readings(s1, s2, s3), expected)

    def test_no_agreement(self):
        s1 = [10, 20, 30]
        s2 = [40, 50, 60]
        s3 = [70, 80, 90]
        expected = [(10+40+70)/3, (20+50+80)/3, (30+60+90)/3]
        self.assertEqual(fuse_readings(s1, s2, s3), expected)

    def test_mixed_cases(self):
        s1 = [1, 2, 3]
        s2 = [1, 2, 4]
        s3 = [1, 3, 5]
        expected = [1, 2, (3+4+5)/3]  
        self.assertEqual(fuse_readings(s1, s2, s3), expected)

    def test_empty_lists(self):
        s1 = []
        s2 = []
        s3 = []
        expected = []
        self.assertEqual(fuse_readings(s1, s2, s3), expected)

    def test_single_element(self):
        s1 = [5]
        s2 = [6]
        s3 = [7]
        expected = [(5+6+7)/3]  
        self.assertEqual(fuse_readings(s1, s2, s3), expected)

if __name__ == "__main__":
    unittest.main()
