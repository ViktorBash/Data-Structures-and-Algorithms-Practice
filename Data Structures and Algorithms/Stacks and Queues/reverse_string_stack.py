from stack_structure import Stack


str_1 = "123456789"
s = Stack()
print(len(s))
for i in range(len(str_1)):
    s.push(str_1[i])

new_str = ""
for i in range(len(s)):
    new_str = new_str + (s.pop())

print(str_1)
print(new_str)
