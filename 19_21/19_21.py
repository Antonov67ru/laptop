def f(x, y, z):
    if (z == 3 or z == 5) and x + y >= 65:
        return 1
    elif z == 5 and x + y < 65:
        return 0
    elif x + y >= 65 and z < 5:
        return 0
    else:
        if (z % 2 == 0):
            return f(x + 1, y, z + 1) or f(x * 3, y, z + 1) or f(x, y + 1, z + 1) or f(x, y * 3, z + 1)
        return f(x + 1, y, z + 1) and f(x * 3, y, z + 1) and f(x, y + 1, z + 1) and f(x, y * 3, z + 1)
for s in range(1, 59):
    if f(s, 6, 1):
        print(s)

# 19) 7
# 20) 10, 19
# 21) 18