"""
Bubble sort in Python
Bubble sort goes through the list and checks if the item on the left is greater or smaller than the item on the right,
and swaps them accordingly.

Slow, good for thousands or tens of thousands, otherwise not good.
Big O Notation: O(n^2)

"""

def bubbleSort(my_list):
    for i in range(0, len(my_list) - 1):
        for j in range(0, len(my_list) -1 - i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list