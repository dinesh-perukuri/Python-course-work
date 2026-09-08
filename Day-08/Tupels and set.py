Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #List collection of elements and kept in peranthasis
>>> t = ()
>>> t = tuple()
>>> t = (1,2,3,4)
>>> t
(1, 2, 3, 4)
>>> t = (1)
>>> t
1
>>> t = (-1)
>>> t
-1
>>> t = (1,1,1,1)
>>> t
(1, 1, 1, 1)
>>> t = (1,23.4, "str", [1,2,3],(1,2,30), {1,2,3}, True)
>>> t
(1, 23.4, 'str', [1, 2, 3], (1, 2, 30), {1, 2, 3}, True)
>>> type(t)
<class 'tuple'>
>>> #Tuple operations concatination repetation
>>> t[1]
23.4
>>> t[-1]
True
>>> t[-3]
(1, 2, 30)
>>> t[2]
'str'
>>> t[3:7]
([1, 2, 3], (1, 2, 30), {1, 2, 3}, True)
>>> t[7]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t[7]
IndexError: tuple index out of range
>>> 23.4 in t
True
>>> "str" in t
True
>>> 'str' in t
True
>>> True in t
True
>>> False in t
False
>>> t
(1, 23.4, 'str', [1, 2, 3], (1, 2, 30), {1, 2, 3}, True)

sorted(t)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'
sorted(t)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'
t = (1548, 966549854, 655, 5465465 ,46544)
t
(1548, 966549854, 655, 5465465, 46544)
sorted(t)
[655, 1548, 46544, 5465465, 966549854]
max(t)
966549854
min(t)
655
len(t)
5
t
(1548, 966549854, 655, 5465465, 46544)
t.index(1548)
0
 t.index(655)
 
SyntaxError: unexpected indent
t.index(655)
2
t.count(655)
1
all(1,2,3)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    all(1,2,3)
TypeError: all() takes exactly one argument (3 given)
all((1,2,3))
True
any((1,2,3,00,0))
True
all((1,2,3,00,0))
False
t = 1,2,3
t
(1, 2, 3)
a,b,c = t
a
1
b
2
c
3
t
(1, 2, 3)
t = (1,2,3,4,5,6,7,8,9,0)
t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
t[4].append(5)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    t[4].append(5)
AttributeError: 'int' object has no attribute 'append'
t[4]
5
t[4].append(5)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    t[4].append(5)
AttributeError: 'int' object has no attribute 'append'
t = (1,2,3,4,4,)
sum(t)
14
#Set is mutable dynamic heteregenous unordered no-duplicates
#Set is mutable dynamic heteregenous unordered no-duplicates
#Mutables are not allowed
s = set()
type(s)
<class 'set'>
s = {1,2,3,4,5,6,1325456,124,2345234.312}
s
{1, 2, 3, 4, 5, 6, 1325456, 2345234.312, 124}
s = {1,1,1,1,1}
s
{1}
s = set()
s.add(1)
s.add(12.3)
a.add("str")
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.add("str")
AttributeError: 'int' object has no attribute 'add'
s.add("str")
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
SyntaxError: invalid syntax
#Set operations
s.add({1:1})
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    s.add({1:1})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add(False)
s
{False, 1, 12.3, 'str'}
#Set operations ^^^^^^^ correct operations
s[0]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s[::1]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    s[::1]
TypeError: 'set' object is not subscriptable
#Union intersection difference membership symmentric sub-set super-set disjoint
a = {1,2,3,4,5}
b = {3,5,7,8,9}
2 in a
True
10 in a
False
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
b -
SyntaxError: invalid syntax
b - a
{8, 9, 7}
a ^ b
{1, 2, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5}
{1}<=a
True
{1,2,3}<=a
True
{1,7,8,9}<=a
False
a>={1,2}
True
a>={1,2}
True
a>={15,16}
False
m={1,2,}
m={1,2,,3}
SyntaxError: invalid syntax
m={1,2,3}

n={4,5,6}
n.isdisjoint(b)
False
#Methods
a ={12,43,1,7,89,,40,23,44}
SyntaxError: invalid syntax
a ={12,43,1,7,89,40,23,44}
a
{1, 7, 40, 43, 12, 44, 23, 89}
sorted(a)
[1, 7, 12, 23, 40, 43, 44, 89]
max(a)
89
min(a)
1
len(a)
8
a.index(a)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
all({1,1,23,43,13,1})
True
any({0,''})
False
any({0,'',(),True})
True
sum(a)
259
a
{1, 7, 40, 43, 12, 44, 23, 89}
a = {1,2,3}
b = a
a
{1, 2, 3}
b
{1, 2, 3}
c = a.copy()
c
{1, 2, 3}
c.add(5)
c
{1, 2, 3, 5}

c
{1, 2, 3, 5}
a
{1, 2, 3}
b.add(999999999999999)
b
{1, 2, 3, 999999999999999}
b.add(659561149)
b
{1, 2, 3, 659561149, 999999999999999}
b.add(100)
b
{1, 2, 3, 100, 659561149, 999999999999999}
b.add(25596521)
b
{1, 2, 3, 100, 25596521, 659561149, 999999999999999}
a.add(23014)
a
{1, 2, 3, 100, 23014, 25596521, 659561149, 999999999999999}
a.add(300)

A
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a
{1, 2, 3, 100, 23014, 25596521, 300, 659561149, 999999999999999}
a.pop(1)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    a.pop(1)
TypeError: set.pop() takes no arguments (1 given)
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
a.add(10,20,30,40)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    a.add(10,20,30,40)
TypeError: set.add() takes exactly one argument (4 given)
a.pop()
1
a.pop()
2
a.pop()
3
a.pop()
100
a.remove(300)
a
{23014, 25596521, 659561149, 999999999999999}
a.remove(99999999999999)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    a.remove(99999999999999)
KeyError: 99999999999999
a.remove(999999999999999)

a
{23014, 25596521, 659561149}
a.discard(100)
a
{23014, 25596521, 659561149}
a.discard(30)
a
{23014, 25596521, 659561149}
a.clear()
a
set()
a = frozenset({1,2,3,4})
a
frozenset({1, 2, 3, 4})
