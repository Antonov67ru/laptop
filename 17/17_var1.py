a = [int(x) for x in open('17-1.txt')]
ans = []
mn = min(a)
for i in range(1, len(a)):
    if a[i-1]%20 + a[i]%20 == mn:
        ans.append(a[i-1]+a[i])
print(len(ans), max(ans)) # 22, 12081