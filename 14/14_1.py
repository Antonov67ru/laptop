for x in range(1, 2031):
    v = 3**100 - x
    s = ''
    while v:
        s += str(v%3)
        v//=3
    if s.count('0')==5:
        print(x) # 2024