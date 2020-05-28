"""
Binary Search in Python for sorted lists. (If the list is not sorted, Binary search is useless and doesn't work).

Notes:
    Binary search is O(logN) because we halve the data we are searching in every step.
    This is more useful than just going through the whole list looking for the target (that is O(n) time).
    You can make this iteratively or recursively.

How To Do Binary Search:
    Split the list in half and check if the element we are looking for is greater or smaller.
    If greater, look in the upper half
    If smaller, look in the smaller half

"""


# Iterative approach
def binary_search_iterative(data, target):
    # Index of the lowest element and highest element in the section we are searching
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2  # Middle of the array (floor division because we use as index)
        if target == data[mid]:
            return True
        elif target < data[mid]:  # Shift the highpoint lower (moving to the left)
            high = mid - 1
        else:
            low = mid + 1  # Shift the low point higher (moving to the right)
    return False


# Recursive approach
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)


if __name__ == "__main__":
    data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    target = 28
    print(binary_search_iterative(data, target))
    print(binary_search_recursive(data, target, 0, len(data) - 1))

    target = -5
    print(binary_search_iterative(data, target))
    print(binary_search_recursive(data, target, 0, len(data) - 1))
