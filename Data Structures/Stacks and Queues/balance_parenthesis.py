"""
Using a stack to balance parenthesis
() {}

(()
Check if parenthesis are balanced or not, input = str

We will loop through the string, analyzing each character, if we have an open parenthesis we push, if we have a closed
one we will pop and check if it matchs.
"""
from stack_structure import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    return False


def parenthesis(input_str):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(input_str) and is_balanced:
        paren = input_str[index]
        if paren in "{[(":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    return False


def main():
    print(parenthesis("()()()"))
    print(parenthesis("[({}){()()}]"))
    print(parenthesis("({)()()"))



if __name__ == "__main__":
    main()
