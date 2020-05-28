"""
Insertion sort in Python.
Insertion sort is not a fast sotring algorithm because it uses nested loops to sort.
It is only good for small datasets.
Big O Notation: O(n^2)


Insertion sort loops through the list, starting at the 2nd element (index 1) to the end.
Expensive Operation: swapping the values

How it works: we loop through all of the elements in the list.
For each element, we loop through everything to the left of it to see if we need to swap two elements.
"""
l1 = [5, 4, 7, 2, 8, 9]


def insertion_sort(a):
    for i in range(1, len(a)):  # Looping through index 1 to the last index
        for j in range(i-1, -1, -1):  # Looping from i-1 to 0 (reverse because -1)
            if a[j] > a[j+1]:  # Checking if smaller/should be moved
                a[j], a[j+1] = a[j+1], a[j]  # Re assigning,
            else:
                break
    return a


print(insertion_sort(l1))


def insertion_sort_2(a):
    for i in range(1, len(a)):  # Same range as before
        j = i-1  # Setting J to i -1
        while a[j] > a[j+1] and j >= 0:  # Same as for loop, we just decrease j by one at the end
            a[j], a[j+1] = a[j+1], a[j]  # Re assigning variables
            j -= 1
    return a


def insertion_sort_better(a):
    for i in range(1, len(a)):  # Looping through index 1 to the last index
        curNum = a[i]
        for j in range(i-1, -1, -1):  # Looping from i-1 to 0 (reverse because -1)
            if a[j] > curNum:
                a[j+1] = a[j]
            else:
                a[j+1] = curNum
                break
    return a