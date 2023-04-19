from unittest import TestCase,main
from parser import split_buildings

class split_buildings_test(TestCase):
    def test_split_buildings_with_commas(self):
        input_str = "Building A,Building B,Building C"
        expected_output = ["Building A", "Building B", "Building C"]
        self.assertEqual(split_buildings(input_str), expected_output)

    def test_split_buildings_empty_input(self):
        input_str = ""
        expected_output = []
        self.assertEqual(split_buildings(input_str), expected_output)

    def test_split_buildings_one_building(self):
        input_str = "Building A"
        expected_output = ["Building A"]
        self.assertEqual(split_buildings(input_str), expected_output)

if __name__=="__main__":
    main()
