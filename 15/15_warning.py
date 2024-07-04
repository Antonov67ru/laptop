def f(x, y):
    return (x + y <= 26) or (y <= x - 4) or (y >= a)
for a in range(100000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a) # 0 1 2 3 4 5 6 7 8 9 10 11 12
        # 12