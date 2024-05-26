# Import the regex.py
import regex

# Define a list of test strings with expected results
test_cases = [
    ("001122", "False"),
    ("001121", "True"),
    ("01010101", "True"),
    ("011", "True"),
    ("20120", "True"),
    ("201112102", "True"),
    ("001101", "False"),
    ("112210", "False"),
    ("011011", "False"),
    ("111012", "False")
]

# Function to run the test cases
def run_tests():
    print("\nRunning tests... \n")
    for input_string, expected in test_cases:
        # Print the input string, expected result, and actual result
        print(input_string, "-> Expected:", expected, "-> Result: ", regex.check(input_string))
        
run_tests()