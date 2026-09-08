Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #List list is collection of elements represented in square braces[]
>>> l  = []
>>> l = list()
>>> type(1)
<class 'int'>
>>> type(l)
<class 'list'>
>>> l = [1,2,3,"str",True,[1,4,8,],)(8,9,10),{1,4,8,}{1:4:5:7},3+8J]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> l = [1,2,3,"str",True,[1,4,8,],(8,9,10),{1,4,8,}{1:4:5:7},3+8J]
SyntaxError: invalid syntax
>>> l = [1,2,3,"str",True,[1,4,8,],(8,9,10),{1,4,8,},{1:4:5:7},3+8J]
SyntaxError: invalid syntax
>>> #Inderxing 0----n -ve Indexing
>>> #Slicing
>>> #Indexing
>>> a = [1,2,3,]
>>> b = [4,5,6]
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> a = [567, 76, 12, 433, 134, 2]
3
>>> 4
4
>>> KeyboardInterrupt
>>> a = [567, 76, 12, 433, 134, 265]
>>> a
[567, 76, 12, 433, 134, 265]
>>> a[-1]
265
>>> a[-5]
76
>>> a[5]
265
>>> a
[567, 76, 12, 433, 134, 265]
>>> a[1:4]
[76, 12, 433]
>>> a[::-1]
[265, 134, 433, 12, 76, 567]
>>> a[1::2]
[76, 433, 265]
>>> a
[567, 76, 12, 433, 134, 265]
76 in a
True
8765 in
SyntaxError: invalid syntax
8765 in a
False
13 in a
False
#List methods
l
[]
a
[567, 76, 12, 433, 134, 265]
max(a)
567
min(a)
12
sorted(a)
[12, 76, 134, 265, 433, 567]
len(a)
6
a.pop(7832132)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.pop(7832132)
IndexError: pop index out of range
id(a)
2192036252032
#Modification
id(a)
2192036252032
a[0]
567
a[0]=56

a
[56, 76, 12, 433, 134, 265]
id(a)
2192036252032
#Append

a[-1] = 23
a
[56, 76, 12, 433, 134, 23]
id(a)
2192036252032
a.append(50)
a
[56, 76, 12, 433, 134, 23, 50]
a.append(60)
a
[56, 76, 12, 433, 134, 23, 50, 60]
a.append(59888)
a
[56, 76, 12, 433, 134, 23, 50, 60, 59888]
#Insert
a
[56, 76, 12, 433, 134, 23, 50, 60, 59888]
a.insert(1,66)
a
[56, 66, 76, 12, 433, 134, 23, 50, 60, 59888]
#Extend
a.extend([1,2,3,4])
a
[56, 66, 76, 12, 433, 134, 23, 50, 60, 59888, 1, 2, 3, 4]
a
[56, 66, 76, 12, 433, 134, 23, 50, 60, 59888, 1, 2, 3, 4]
#POP
a.pop(-5)
59888
a.pop(0)
56
a
[66, 76, 12, 433, 134, 23, 50, 60, 1, 2, 3, 4]
a.pop(2)
12
a.pop(5)
50
#Remove
a.remove(23)
a
[66, 76, 433, 134, 60, 1, 2, 3, 4]
a.remove(0)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.remove(0)
ValueError: list.remove(x): x not in list
a.remove(60)
a
[66, 76, 433, 134, 1, 2, 3, 4]
a.remove(66)
a
[76, 433, 134, 1, 2, 3, 4]
#Delete
del a[1]
a
[76, 134, 1, 2, 3, 4]
#Clear
a.clear()
a
[]
#List methods
# any, all, append, copy, sum, sorted, list, append, extend, sorted, reverse, asssing, desining
a.index(13)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.index(13)
ValueError: list.index(x): x not in list
a
[]
a = (1,2,3,4)
a
(1, 2, 3, 4)
a.index(2)
1
a.index(13)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.index(13)
ValueError: tuple.index(x): x not in tuple
a.count(50)
0
a = [1,2,3,4]
a
[1, 2, 3, 4]
b = a
a
[1, 2, 3, 4]
b.append(7)
a
[1, 2, 3, 4, 7]
b
[1, 2, 3, 4, 7]
c = a.copy()
a
[1, 2, 3, 4, 7]
b
[1, 2, 3, 4, 7]
c.append(12)
c
[1, 2, 3, 4, 7, 12]
a
[1, 2, 3, 4, 7]
any([1,'',"",False,[],{},(),set,<>,})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
any([1,'',"",False,[],{},(),set,<>,])
SyntaxError: invalid syntax
any([1,'',"",False,[],{},(),set,)<>),])
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
any([1,'',"",False,[],{},(),set,(<>),])
SyntaxError: invalid syntax
any([1,'',"",False,[],{},(),set,])
True
sum(a)
17
a
[1, 2, 3, 4, 7]
l.sort()
l
[]
a.sort()
a
[1, 2, 3, 4, 7]
a.reverse()
a
[7, 4, 3, 2, 1]
