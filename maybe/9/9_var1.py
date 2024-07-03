k = 0
for s in open('9.txt'):
    a = sorted(map(int, s.split()))
    if a[-1] < a[0]+a[1]+a[2]:
        if len(set(a)) == 3:
            k += 1
print(k)