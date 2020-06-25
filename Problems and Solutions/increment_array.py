"""
You are given an array, ex: [5, 2, 7, 2]. Pretend it is a number (5272), and that you must increment it by one. Return
the array.
Examples:
    [5, 2, 7, 2] --> [5, 2, 7, 3]
    [9, 9, 9] --> [1, 0, 0, 0]
    [5, 2, 9] --> [5, 3, 0]

All values in array are 0-9, and array will not be empty.
"""

def return_number(arr):
    if arr[-1] < 9:
        arr[-1] += 1
        return arr
    else:
        for i in range(len(arr)-1, -1, -1):
            if arr[i] >= 9:
                arr[i] = 0
                if i-1 >= 0:
                    arr[i-1] += 1
                else:
                    arr.insert(0, 1)
        return arr


if __name__ == "__main__":
    arr1 = [5, 2, 7, 2]
    arr2 = [9, 9, 9]
    arr3 = [5, 2, 9]
    print(return_number(arr1))
    print(return_number(arr2))
    print(return_number(arr3))
