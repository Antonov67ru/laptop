#v1code

file = open('26_2024_1.txt')

n, r, m = [int(x) for x in file.readline().split()]
a = []
for i in range(n):
    s = file.readline().split()
    a.append((int(s[0]), int(s[1])))
for i in range(1, m + 1):
    a.append((r + 1, i))
for i in range(1, m + 1):
    a.append((0, i))

a.sort(key=lambda t: (t[1], t[0]))

max_free = -10 ** 20
min_ry = 10 ** 20
ans = []
for i in range(1, len(a)):
    if a[i - 1][1] == a[i][1]:
        cur_ryd = a[i][0] - 1
        count_free = a[i][0] - a[i - 1][0] - 2
        if count_free > max_free:
            max_free = max(max_free, count_free)
            min_ry = cur_ryd
        if count_free == max_free:
            min_ry = min(min_ry, cur_ryd)

print(min_ry, max_free)

#v2code

file = open('26_2024_1.txt')

n, r, m = [int(x) for x in file.readline().split()]
a = []
for i in range(n):
    s = file.readline().split()
    a.append((int(s[0]), int(s[1])))
for i in range(1, m+1):
    a.append((r+1, i))
for i in range(1, m+1):
    a.append((0, i))

a.sort(key=lambda t: (t[1],t[0]))
print(a)
ans = []
for i in range(1, len(a)):
    if a[i-1][1] == a[i][1]:
        ans.append((a[i][0] - 1, a[i][0] - a[i-1][0] - 2))

max_raz = -10**20
for ry, raz in ans:
    if raz > max_raz:
        max_raz = raz

min_ry = 10**20
for ry, raz in ans:
    if raz == max_raz:
        min_ry = min(min_ry, ry)

print(min_ry, max_raz)
print()

