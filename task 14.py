n = int(input())
z = 0
p = 0
n = 0
for i in range(n):
    x = int(input())
    if x == 0:
        z += 1
    elif x > 0:
        p += 1
    else:
        n += 1
print(z, p, n)
