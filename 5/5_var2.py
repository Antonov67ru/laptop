ans = []
for n in range(1, 13):
    n2 = f'{n:b}'
    if n%2==0:
        n2 = '10' + n2
    else:
        n2 = '1' + n2 + '01'
    ans.append(int(n2,2))
print(max(ans))
# 109