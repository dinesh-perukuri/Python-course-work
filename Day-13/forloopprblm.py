'''
n = int(input("Enter the input: "))
res = []
for i in range(1,n+1):
    if n%i==0:
        res.append(i)

print(f'Factors of {n} = {res}')
'''

'''
s = 'Dinesh  Perukuri'
d = {'D': 1, 'i': 2, 'n': 1, 'e': 2, 's': 2, 'h': 1, ' ': 1, 'P': 1, 'r': 1, 'u': 1, 'k': 1}
print(d)
'''

'''
s = 'Paradise'
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)


s = 'aaaaaassssssssssddddddddddfffffffffqqqqqqqaaaaaaa'
c=1
res = ''
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c += 1
    else:
        res += str(c) + s[i]
        c=1
print(res+s[i]+str(c))
'''


pass 
