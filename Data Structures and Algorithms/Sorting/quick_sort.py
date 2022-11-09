"""
Quicksort in Python
Pivot: number we are comparing everything to
Left partition: left to pivot value
Right partition: right to pivot value
Often the first item is used for the pivot, it can also be the last or the middle item
Or you can choose the median of the first, last and middle value as your pivot point

The border has everything less than the pivot, and at the end the one of the border values and the pivot swap
Quicksort is recursive, so it keeps splitting up and sorting until the lists get to 1 item.
Very efficient on large datasets, hugely relies on pivot selection for efficiency.
Worst case scenario: O(n^2)
Average case: O(n log n)

6:21
"""


def quick_sort(a):
    quick_sort2(a, 0, len(a) - 1)


def quick_sort2(a, low, hi):
    if low < hi:
        p = partition(a, low, hi)
        quick_sort2(a, low, p - 1)
        quick_sort2(a, p + 1, hi)


def get_pivot(a, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if a[low] < a[mid]:
        pivot = mid
    elif a[low] < a[hi]:
        pivot = low
    return pivot


def partition(a, low, hi):
    pivotIndex = get_pivot(a, low, hi)
    pivotValue = a[pivotIndex]
    a[pivotIndex], a[low] = a[low], a[pivotIndex]
    border = low

    for i in range(low, hi + 1):
        if a[i] < pivotValue:
            border += 1
            a[i], a[border] = a[border], a[i]
    a[low], a[border] = a[border], a[low]
    return border


def new_quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        first_part = new_quicksort(x[:i])
        second_part = new_quicksort(x[i + 1:])
        first_part.append(x[i])
        return first_part + second_part


def best_quicksort(x):
    if len(x) < 2:
        return x
    else:
        pivot = x[0]
        less = [i for i in x[1:] if i <= pivot]
        greater = [i for i in x[1:] if i > pivot]
        return best_quicksort(less) + [pivot] + best_quicksort(greater)


arr = [12, 11, 13, 5, 6, 7]
print(arr)
print(best_quicksort(arr))
