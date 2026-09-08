'''
#initialization, condtion, update.
i = 1
while i<=10:
    print(i)
    i+=1
    '''
'''
i = 10
while i>10:
    print(i)
    i-=1
    '''

'''
i = 5
while i<=50:
    print(i)
    i+=
    '''
'''
s = 'while loop'
i = 0
while i<len(s):
    print(s[i])
    i+=1
    '''
'''
s = 'while loop'
i = 0
while i<len(s):
    print(s[i])
    i-=1
    '''
'''
l =[5467,5678,6789,987]
i = 0
while i<len(l):
    print(l[i])
    i+=1
    '''
'''
''n = 987456321
while n>0:
    print(n%10)
    n//=10
'''

'''
n = 987654321
sumofdigits = 0
while n>0:
    sumofdigits += n%10
    n//=10

print("sum of digits:", sumofdigits)
'''

'''
n = 987654321
sumreate a carofdigits = 0
while n>0:
    sumofdigits *= n%10
    n//=10

print("sum of digits:", sumofdigits)
'''
'''
n = 98745
res=0
while n > 0:
    rem = n%10
    res = res*10 + rem
    n//=10
print(res)
'''
'''
n = 876543456
res=0
while n>0:
    rem = n%10
    if rem%2==0:
        res += rem
    n//=10
print(res)
'''

'''
l = [7,9,8,4,5,7,84,12,45,14,0,1,2,0,1,4,5,6,8,88,66,33,5,3,0]
i = 0
while i < len(l):
    if l[i] == 0:
        l.pop(i)
    else:
        i += 1
print(l)
'''

'''
l = [7,9,8,4,5,7,84,12,45,14,0,1,2,0,1,4,5,6,8,88,66,33,5,3,0]
while 0 in l:
    l.remove(0)
print(l)
'''

'''
l = [2,4,6,8,10,36,24,56,38,67,98,99]
i,j = 0, len (l)-1
while i <= j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1
    '''