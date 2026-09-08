'''
import sys
print(sys.argv)
print(sys.version)
print(sys.path)
print("start")
sys.exit()
print("end")
'''

'''

import platform 

print(platform.system())
print(platform.release())
print(platform.processor())
'''

'''
import math

print(math.pi)
print(math.e)

print(math.log(2,2))
print(math.sin(30))
print(math.cos(60))
print(math.tan(45))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.gcd(9,12))
print(math.sqrt(25))
print(math.pow(2,3))
'''

'''
import math 

print(round(12.02565))
print(round(000000.55))
print(round(15.0000008))
print(round(12.000000009))


print(math.ceil(12.02565))
print(math.ceil(000000.55))
print(math.ceil(15.0000008))
print(math.ceil(12.00000009))

print(math.floor(12.02565))
print(math.floor(000000.55))
print(math.floor(15.0000008))
print(math.floor(12.00000009))
'''

'''
import random

print(random.seed())
print(random.randint(100000,999999))
print(random.uniform(1,6))

l = ['R','P','S']
print(random.choice(l))

name = ['Dinesh','Rasool','Ranjith','Vikky']
print(random.choices(name,k=2))

random.shuffle(name)
print(name)
'''

'''
from collections import Counter

s ='Python Programming'
res = Counter(s)
print(res)

d={}

for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''

'''
from collections import Counter,defaultdict

products = ['Sugar','Wheat','chicken']
res = defaultdict(list)

for i in products:
    res[i].append(['des','rev','com'])

print(res)

s = 'Python Programming'

d = defaultdict(int)

for i in s:
    d[i]+=1

print(d)
'''
'''
from collections import Counter,defaultdict,deque

l = deque([])

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()
print(l)
'''