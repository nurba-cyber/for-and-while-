x = int(input())

v = 0
while x > 0:
    v = v * 10 + x % 10
    x //= 10
print(v)
