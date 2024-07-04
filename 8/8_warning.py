from itertools import *
k = 0
for s in product("0123456789ABCDEFG", repeat = 5):
    s = ''.join(s)
    if s[0] != "0" and s.count("3") == 1:
        for el in "DEFG": s = s.replace(el, "D")
        if s.count("D") >= 3:
            k += 1
print(k) # 16384