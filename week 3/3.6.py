a = list(map(int, input().split()))
print('NO')
for i in range(1, len(a)):

        if a[i] in a[0:i]:
            print('YES')
        else:
            print('NO')