"""
Calculate string length with recursion in Python

When making a recursive function:
What is the base case
What are the recursive calls
"""

input_str = "ViktorBasharkevich"
print(len(input_str))


def iterative_str_len(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count

def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1::])

print(iterative_str_len(input_str))
print(recursive_str_len(input_str))