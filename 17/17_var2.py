a = [int(x) for x in open('17-2.txt')]
k = sum(x%32==0 for x in a)
ans = []
for i in range(1, len(a)):
    if a[i-1] < 0 or a[i] < 0:
        if a[i-1]+a[i] < k:
            ans.append(a[i-1]+a[i])
print(len(ans), max(ans))