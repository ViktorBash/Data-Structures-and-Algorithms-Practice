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
    quick_sort2(a, 0, len(a)-1)


def quick_sort2(a, low, hi):
    if low < hi:
        p = partition(a, low, hi)
        quick_sort2(a, low, p-1)
        quick_sort2(a, p + 1, hi)


def get_pivot(a, low, hi):
    mid = (hi + low)//2
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

    for i in range(low, hi+1):
        if a[i] < pivotValue:
            border += 1
            a[i], a[border] = a[border], a[i]
    a[low], a[border] = a[border], a[low]
    return border


arr = [12, 11, 13, 5, 6, 7]
quick_sort(arr)
print(arr)