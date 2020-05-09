"""
Selection sort in Python
This algorithm looks for the smallest item in the whole list. After done searching, it swaps this to the left, and
repeats.

Selection sort is not a fast sorting algorithm because it uses nested loops to sort.
It is useful only for small data sets.
Big O notation: O(n^2)

How it works:
Iterate through whole list skipping last index.
minIndex = i (setting what is the minimum value as we go through)
Then we loop through the rest of the list remaining, setting minIndex = j if it is less than the current min index
After running through all of the second for loop, we swap the item if need be/

"""
l1 = [5, 4, 7, 2, 8, 9]


def selection_sort(a):
    for i in range(0, len(a) - 1):
        minIndex = i
        for j in range(i+1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        if minIndex != i:  # Swaps if we found number lower than i
            a[i], a[minIndex] = a[minIndex], a[i]
    return a


print(selection_sort(l1))
