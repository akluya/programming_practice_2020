a = set()
n = input()
for i in range(int(n)):
    a.update(input().split())
print(len(a))