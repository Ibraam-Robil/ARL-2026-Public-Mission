import unittest
from Lane_maneuvers import analyze_drive   

class TestAnalyzeDrive(unittest.TestCase):

    def test_no_changes(self):
        lanes = [1, 1, 1, 1, 1]
        self.assertEqual(analyze_drive(lanes), (0, 0))

    def test_single_change(self):
        lanes = [1, 1, 2, 2, 2]
        self.assertEqual(analyze_drive(lanes), (1, 0))

    def test_multiple_changes(self):
        lanes = [0, 1, 0, 1, 0]
        self.assertEqual(analyze_drive(lanes), (4, 0))

    def test_dangerous_maneuver(self):
        lanes = [0, 2]
        self.assertEqual(analyze_drive(lanes), (1, 1))

    def test_dangerous_and_safe_mix(self):
        lanes = [0, 1, 2, 0, 2]
        self.assertEqual(analyze_drive(lanes), (4, 2))

    def test_short_input(self):
        self.assertEqual(analyze_drive([]), (0, 0))
        self.assertEqual(analyze_drive([1]), (0, 0))


if __name__ == "__main__":
    unittest.main()
