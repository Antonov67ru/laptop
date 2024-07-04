f = open('27A.txt')
n = int(f.readline())
a = [int(el) for el in f]
res = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for m in range(k+1, n):
                res += [sum(a[i:j+1]) + sum(a[k:m+1])]
print(max(res))
# НА ФАЙЛ Б
mxB = -float('inf')
pref_sum = [0] * (n+1)
pref_left = [0] * (n+1)
pref_right = [0] * (n+1)
pref_RT = [-float('inf')] * (n+1)
for i in range(n):
     pref_sum[i] = pref_sum[i-1] + a[i]
     pref_left[i] = min(pref_left[i-1], pref_sum[i])
for i in reversed(range(n)):
     if i <= n - 2:
          pref_RT[i] = max(pref_RT[i+1], pref_sum[n-1] - pref_sum[i-1] - pref_right[i+2])
     pref_right[i] = min(pref_right[i+1], pref_sum[n-1] - pref_sum[i-1])
for i in range(1, n-2):
     mxB = max(mxB, pref_sum[i] - pref_left[i-2] + pref_RT[i+1])
print(mxB)
