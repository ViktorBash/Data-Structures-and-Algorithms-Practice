t = int(input())
for i in range(1, t + 1):
    l, r = [int(s) for s in input().split(" ")]
    total = r - l + 1
    for j in range(l, r + 1):
        for k in range(len(str(j))):
            num = int(str(j)[k])
            if num % 2 == 0 and (k + 1) % 2 == 1:
                total -= 1
                break
            elif num % 2 == 1 and (k + 1) % 2 == 0:
                total -= 1
                break
    print(f"Case #{i}: {total}")


# Old Attempt:
# t = int(input())
# for i in range(1, t + 1):
#     l, r = [int(s) for s in input().split(" ")]
#     total = r - l + 1
#     for j in range(l, r + 1):
#         for k in range(len(str(j))):
#             num = int(str(j)[k])
#             if num % 2 == 0 and (k + 1) % 2 == 1:
#                 total -= 1
#                 break
#             elif num % 2 == 1 and (k + 1) % 2 == 0:
#                 total -= 1
#                 break
#     print(f"Case #{i}: {total}")
