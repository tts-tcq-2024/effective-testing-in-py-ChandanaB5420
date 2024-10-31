major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def print_color_map():
    for i in range(5):
        for j in range(5):
            pair_number = i * 5 + j
            print(f"{pair_number:2} | {major_colors[i]:6} | {minor_colors[j]:6}")
    return 25

def test_print_color_map():
    from io import StringIO
    import sys

    # Capture the output of print_color_map
    actual_output = StringIO()
    sys.stdout = actual_output

    print_color_map()
    
    sys.stdout = sys.__stdout__  # Restore original stdout

    # Build the expected output
    expected_output = ""
    for i in range(5):
        for j in range(5):
            pair_number = i * 5 + j
            expected_output += f"{pair_number:2} | {major_colors[i]:6} | {minor_colors[j]:6}\n"

    # Test if the output matches the expected output
    assert actual_output.getvalue() == expected_output, "Test failed: Output is not correctly aligned or mapped."

def main():
    result = print_color_map()
    assert result == 25
    test_print_color_map()
    print("All is well (maybe!)")

if __name__ == "__main__":
    main()

