"""
Author: Valeria Zúñiga Mendoza
Date: 26/05/2024
Project: E1 Implementation of Lexical Analysis (Regular Expression)

Purpose of the project: 
Check if numbers belong to the language specified by the Regular Expression.
Where it accepts all the posible combinations of 0, 1, 2, 
that don't contain 1011, 1012, 1101, 1122.
"""

import re


def check(input_string):
    # Define the Regular expression pattern
    regex = r'(?!.*1101|.*1122|.*1011|.*1012)[012]+'

    # Verify if it matches with the regex
    match = re.fullmatch(regex, input_string)
    return bool(match)


def main():
    print("\nEnter a string using 0, 1, 2. \nDon't include 1011, 1012, 1101, 1122.") 

    input_string = input("\nCheck: ")
    if check(input_string):
        print(input_string, "-> Accepted")
    else:
        print(input_string, "-> Rejected")

if __name__ == "__main__":
    main()