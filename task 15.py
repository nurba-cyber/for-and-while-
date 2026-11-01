n = int(input())
h = False
for i in range(n):
    x = int(input())
    if x == 0:
        h = True
if h:
    print("YES")
else:
    print("NO")
