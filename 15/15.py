def f(x, a):
    B = 70 <= x <= 90
    return (x%a==0) or (B <= (x%22!=0))

for a in range(1000, 0, -1):
    if all(f(x,a) for x in range(1, 10000)):
        print(a) # 88
        break