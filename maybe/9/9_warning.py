k = 0
for s in open("test.txt"):
    a = [int(el) for el in s.split()]
    r2 = [el for el in a if a.count(el) == 2]
    r1 = [el for el in a if a.count(el) == 1]
    if len(r2) == 2 * 2 and len(r1) == 2 * 1:
        if sum(r2) < sum(r1):
            k += 1
print(k)