"""
Google CodeJam
"""


def compute(arr):
    computations = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            if len(str(arr[i])) == len(str(arr[i-1])):
                arr[i] = int(str(arr[i]) + "0")
                computations += 1
            elif int(str(arr[i])[0]) < int(str(arr[i-1])[0]):
                old = arr[i]
                new = str(arr[i])
                for j in range(0, len(str(arr[i - 1])) - len(str(arr[i])) + 1):
                    new = new + "0"
                arr[i] = int(new)
                computations += len(new) - len(str(old))
            elif int(str(arr[i])[0]) == int(str(arr[i-1])[0]):
                mega_old = arr[i]
                not_done = True
                while not_done:
                    for l in range(len(str(arr[i-1]))):
                        not_done = False
                        old = arr[i]
                        if len(str(arr[i])) == l:  # Big problem area
                            stop = False
                            disqualiefied = True
                            for b in range(len(str(arr[i-1])) - len(str(arr[i]))):
                                if int(str(arr[i-1])[b + l]) != 9:
                                    disqualiefied = False
                            if disqualiefied:
                                new = str(arr[i])
                                for b in range(len(str(arr[i - 1])) - len(str(arr[i]))):
                                    new += "0"
                                new += "0"
                                arr[i] = int(new)
                                break
                                # print(new)
                            for b in range(len(str(arr[i-1])) - len(str(arr[i])) - 1):
                                if int(str(arr[i-1])[b + l + 1]) == 9:
                                    arr[i] = int(str(arr[i]) + "1")
                                    for c in range(len(str(arr[i])) - l - b):
                                        arr[i] = int(str(arr[i]) + "0")
                                    not_done = False
                                    stop = True
                                    break
                            if stop:
                                break
                            # print(arr[i-1])
                            second_part = str(arr[i-1])[len(str(arr[i])):]
                            last_part_of_second_part = int(second_part[-1]) + 1
                            final_part = second_part[0:-1] + str(last_part_of_second_part)
                            # print("FINAL PART")
                            # print(final_part)
                            # print(arr[i-1])
                            arr[i] = int(str(arr[i]) + final_part)
                            not_done = False
                            break
                        elif int(str(arr[i])[l]) > int(str(arr[i-1])[l]):
                            new = str(arr[i])
                            for a in range(0, len(str(arr[i-1])) - len(str(arr[i]))):
                                new = new + "0"
                            arr[i] = int(new)
                            not_done = False
                            break
                        elif int(str(arr[i])[l]) < int(str(arr[i-1])[l]):
                            new = str(arr[i])
                            for j in range(0, len(str(arr[i - 1])) - len(str(arr[i])) + 1):
                                new = new + "0"
                            arr[i] = int(new)
                            not_done = False
                            break
                computations += len(str(arr[i])) - len(str(mega_old))
            else:  # i > i-1, > > > > >
                yee_old = arr[i]
                new = str(arr[i])
                for j in range(0, len(str(arr[i-1])) - len(str(arr[i]))):
                    new = new + "0"
                arr[i] = int(new)
                computations += len(str(arr[i])) - len(str(yee_old))
    # print(arr)
    return computations




t = int(input())
for i in range(1, t + 1):
    length = int(input())
    arr = [int(s) for s in input().split(" ")]
    print(f"Case #{i}: {compute(arr)}")
