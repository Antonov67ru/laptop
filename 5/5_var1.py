for n in range(1, 1000):
    n2 = f'{n:b}'
    if n2.count('1') % 2 == 0:
        n2 = '10' + n2[2:] + '0'
    else:
        n2 = '11' + n2[2:] + '1'
    r = int(n2, 2)
    if r > 50:
        print(n)
        break
# 19