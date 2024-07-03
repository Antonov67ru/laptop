s = open('24-3.txt').read().strip()
ps = ['--', '**', '-*', '*-', '-0', '*0', '- ', ' -', '* ', ' *']
for c in ps:
    while c in s: s = s.replace(c,' ')

s = s.split()
for i in range(len(s)):
    while len(s[i])>0 and s[i][0] == '0':
        if len(s[1])==1: s[i]=''
        else: s[i] = s[i][1:]

print(max(len(c) for c in s)) # 40