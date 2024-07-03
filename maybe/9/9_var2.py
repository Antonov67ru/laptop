cnt = 0
for s in open('9-2.txt'):
    a = list(map(int, s.split()))
    p = [x for x in a if a.count(x)==3]
    np = [x for x in a if a.count(x)==1]
    if len(p) == len(np) == 3:
        if sum(p)**2 > sum(np)**2:
            cnt += 1
print(cnt)