t = int(input())
for i in range(1, t + 1):
    n, k, s = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    # print(f"N: {n}, K: {k}, S: {s}")
    scenario_1_time = 0
    scenario_2_time = 0

    # Calculate 1st scenario (go back, then finish game)
    scenario_1_time += (k - 1)
    scenario_1_time += (k - s)
    scenario_1_time += (n - s + 1)

    # Calculate 2nd scenario (restart game)
    scenario_2_time += k + n

    if scenario_1_time <= scenario_2_time:
        print(f"Case #{i}: {scenario_1_time}")
    else:
        print(f"Case #{i}: {scenario_2_time}")
