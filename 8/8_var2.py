from itertools import *
for i, sl in enumerate(product(sorted('фокус'), repeat=5), 1):
    s = ''.join(sl)
    if 'ф' not in s and s.count('у') == 2:
        nmb = i
print(nmb)
# 2313