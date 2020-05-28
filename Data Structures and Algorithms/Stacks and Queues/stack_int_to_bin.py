"""
Converting integer values to binary with a stack.
We will divide by two to get the binary value
The remainders are the binary representation, (we use stack cause it needs to be reversed)
Ex: 242

242/2 = 121 --> 0 remainder
121 // 2 = 60 --> 1 remainder
and so on
"""

from stack_structure import Stack


def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:

        s.push(dec_num % 2)
        dec_num = dec_num // 2

    bin_int = ""
    while not s.is_empty():
        bin_int += str(s.pop())
    # print(bin_int)
    return bin_int


def main():
    print(div_by_2(242))


if __name__ == "__main__":
    main()


