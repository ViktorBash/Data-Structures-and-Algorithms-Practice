"""
Tribonacci
"""
a, b, c = 0, 0, 1
for i in range(10):
    a, b, c = b, c, c + b + a
    print(c)
