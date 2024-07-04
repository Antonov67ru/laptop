for x in range(1, 2031):
    n = 9**190 + 9**100 - x
    k = 0
    while n > 0:
        if n % 9 == 0:
            k += 1
        n //= 9
        if(k==93):
            print(x) # 729 and 1458  = 729