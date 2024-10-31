import io
import sys

def test_print_color_map():
    # Expected output
    expected_output = ""
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    
    for i in range(len(major_colors)):
        for j in range(len(minor_colors)):
            expected_output += f'{i * 5 + j} | {major_colors[i]} | {minor_colors[j]}\n'

    # Capture the output of print_color_map
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function to test
    result = print_color_map()

    # Restore original stdout
    sys.stdout = sys.__stdout__

    # Get the actual output
    actual_output = captured_output.getvalue()

    # Assert the output matches the expected output
    assert actual_output == expected_output, f"Test failed: Expected output did not match actual output.\nExpected:\n{expected_output}\nActual:\n{actual_output}"

    # Assert the result is correct
    assert result == 25, "Test failed: The return value is not correct."

# Run the test
test_print_color_map()
print("All tests passed successfully!")
