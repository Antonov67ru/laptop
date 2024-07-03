from itertools import *
k = 0
for i in product('01234567', repeat=5):
    s = ''.join(i)
    if s[0] not in '01357' and s[-1] not in '26' and s.count('7') <= 2:
        k += 1
print(k)
# 9135