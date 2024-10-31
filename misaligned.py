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

# Stub for the print_color_map function
def stub_print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    output = ""
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            output += f'{i * 5 + j} | {major} | {minor}\n'
    return output, len(major_colors) * len(minor_colors)

def test_print_color_map():
    # Capture the output of the original print_color_map
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the original function
    result = print_color_map()

    # Restore original stdout
    sys.stdout = sys.__stdout__

    # Get the actual output
    actual_output = captured_output.getvalue()

    # Use the stub to get the expected output
    expected_output, expected_result = stub_print_color_map()

    # Assertions to check if the actual output matches the expected output
    assert actual_output == expected_output, (
        "Test failed: Output does not match the expected format.\n"
        f"Expected:\n{expected_output}Actual:\n{actual_output}"
    )

    # Assert that the return value is correct
    assert result == expected_result, "Test failed: The return value is not correct."

# Run the test
test_print_color_map()
print("All tests passed successfully!")
