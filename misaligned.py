import io
import sys

# Original function
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)
    
import unittest
from unittest.mock import patch
from io import StringIO

# Mock structure to store information about print calls
class PrintfMock:
    def __init__(self):
        self.call_count = 0
        self.buffer = ""

    def mock_print(self, *args, **kwargs):
        self.call_count += 1
        self.buffer += " ".join(str(arg) for arg in args) + "\n"


def print_color_map(mock_print):
    major_color = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_color = ["Blue", "Orange", "Green", "Brown", "Slate"]

    for i in range(5):
        for j in range(5):
            mock_print(f"{i * 5 + j} | {major_color[i]} | {minor_color[j]}")
    return i * j + 1  # Total number of printed lines


class TestPrintColorMap(unittest.TestCase):
    def test_print_color_map(self):
        mock = PrintfMock()

        # Call the function we want to test
        result = print_color_map(mock.mock_print)

        # Check the number of print calls
        self.assertEqual(result, 25)
        self.assertEqual(mock.call_count, 25)  # Check if it called print 25 times

        # Analyze the captured output to find inconsistencies
        expected_pairs = 25  # We expect 25 color pairs
        actual_pairs = 0
        lines = mock.buffer.strip().split("\n")

        for line in lines:
            if "Blue" in line or "Orange" in line or \
               "Green" in line or "Brown" in line or \
               "Slate" in line:
                actual_pairs += 1

        # Fail the test if the actual pairs do not match the expected behavior
        self.assertEqual(actual_pairs, expected_pairs)  # This will fail if the implementation is incorrect


if __name__ == "__main__":
    unittest.main()

