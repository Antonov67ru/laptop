for x in range(2030, 0, -1):
    s = 7**91 + 7**160 - x
    cnt = 0
    while s:
        cnt += s%7==0
        s//=7
    if cnt == 70:
        print(x) # 2029
        break