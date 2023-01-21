# Write a function that takes a string of parentheses,
# and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
# Furthermore, the input string may be empty and/or not contain any parentheses at all.
# Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).


def valid_parentheses(string: str) -> bool:
    if len(string) == 0:
        return True
    if "(" in string and ")" in string:
        idx_left = [i for i, c in enumerate(string) if c == "("]
        idx_right = [i for i, c in enumerate(string) if c == ")"]

        if len(idx_left) == len(idx_right):
            for i, _ in enumerate(idx_left):
                if idx_left[i] > idx_right[i]:
                    return False
            return True
    return False


if __name__ == "__main__":
    print(valid_parentheses("(())((()())())"))
