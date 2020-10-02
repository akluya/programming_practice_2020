a = [int(s) for s in input().split()]
k = 0
n = []

for i in range (len(a)):
    k = a.count(a[i])
    if k == 1:
        n.append(a[i])

print(n)