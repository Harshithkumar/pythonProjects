def is_valid(s: str) -> bool:
    # Dictionary to match opening and closing brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    # Stack to keep track of opening brackets
    stack = []

    # Iterate through each character in the string
    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop the top element from the stack if it is not empty, otherwise assign a dummy value '#'
            top_element = stack.pop() if stack else '#'

            # If the top element does not match the expected opening bracket, return False
            if bracket_map[char] != top_element:
                return False
        else:
            # If it is an opening bracket, push it to the stack
            stack.append(char)

    # If the stack is empty, all brackets were matched properly, otherwise it's invalid
    return not stack


# Test cases

#print(is_valid("(]"))  # Output: False

print(is_valid("{[]}"))  # Output: True
