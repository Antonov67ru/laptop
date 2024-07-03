File = open(name)
N = int(File.readline())
a = [int(x) for x in File]
# Список максимальных чисел в порядке слева направо (для числа S_i)
sp_i = [-10**10]*N
curMx = -10**10
for i in range(N):
    curMx = max(curMx, a[i])
    sp_i[i] = curMx
# Список максимальных чисел в порядке справа налево (для числа S_k)
sp_k = [-10**10]*N
curMx = -10 ** 10
for k in range(N-1, -1, -1):
    curMx = max(curMx, a[k])
    sp_k[k] = curMx
res = 0
for j in range(1, N-1): # Перебор числа S_j
# Для текущего числа S_j:
# максимальный S_i это sp_i[j-1]
# максимальный S_k это sp_k[j+1]
    if a[j] < sp_i[j-1] and a[j] < sp_k[j+1]: # Если (S_j < S_i и S_j < S_k)
        res = max(res, (sp_i[j-1] - a[j]) + (sp_k[j+1] - a[j]))
print(res)