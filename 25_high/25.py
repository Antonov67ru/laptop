def f(x):
    d = set(); sq = round(x**.5)
    for i in range(2, sq+1):
        if x%i==0: d |= {i, x//i}
    if len(d)>0 and (min(d) + max(d)) % 10 == 4:
        return min(d) + max(d)
    return 0

k = 0
for x in range(700001, 10 ** 10):
    if f(x):
        k += 1
        print(x, f(x))
        if k==5: break

# 700004   350004
# 700009   41194
# 700023   233344
# 700024   350014
# 700044   350024