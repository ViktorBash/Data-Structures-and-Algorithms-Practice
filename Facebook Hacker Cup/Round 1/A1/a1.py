# Left hand: F X
# Right hand: F O


def solution(string: str):
    if len(string) <= 1:
        return 0
    switch_amount = 0
    cur_hand_left = True

    for i in range(len(string)):
        if string[i] == "X":
            cur_hand_left = True
            break
        elif string[i] == "O":
            cur_hand_left = False
            break

    for i in range(len(string)):
        if string[i] == "F":
            pass
        elif string[i] == "O":
            if cur_hand_left is True:
                cur_hand_left = False
                switch_amount += 1
        elif string[i] == "X":
            if cur_hand_left is False:
                cur_hand_left = True
                switch_amount += 1
    return switch_amount


def get_input():
    f = open("weak_typing_chapter_1_input.txt", "r")
    test_cases = int(f.readline())
    strings = []
    for line in f:
        try:
            number = int(str(line).strip())
        except Exception:
            result = str(line).strip()
            strings.append(result)
    # print(strings)
    f.close()

    f = open("real_solutions.txt", "w")
    for i in range(len(strings)):
        result = solution(strings[i])
        f.write(f"Case #{i + 1}: {result}\n")
    f.close()


get_input()

