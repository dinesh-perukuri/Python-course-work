Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data type
#int float complex
a = 12
type(a)
<class 'int'>
b = 13.4
type(b)
<class 'float'>
c = 12+4j
type(c)
<class 'complex'>
c = 12
c = 12+6j
c
(12+6j)
# str list tuple
s = 'Codegnan'
id(s)
2382829123888
s += 'Python'
s
'CodegnanPython'
id(s)
2382792068592
s='aaaaaa'
s
'aaaaaa'
type(s)
<class 'str'>
l = [1,2,3,4,5,6,]
type(l)
<class 'list'>
id(l)
2382828979648
l.append(12)
l
[1, 2, 3, 4, 5, 6, 12]
l.append(90)
l
[1, 2, 3, 4, 5, 6, 12, 90]
id(l)
2382828979648
l = [1,12,.3"str",[1,23]]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l = [1,12.3,"str",[1,23]]
l
[1, 12.3, 'str', [1, 23]]
[1, 2, 3, 4, 5, 6, 12]
[1, 2, 3, 4, 5, 6, 12]
type(1)
<class 'int'>
type(t)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    type(t)
NameError: name 't' is not defined
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,12.3,4"c")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
c
(12+6j)
t
(1, 1, 1, 1, 1)
t=(1,12.3,4,"c")
t
(1, 12.3, 4, 'c')
# set dict
s= {80,70,24,14,12,15,10,101,10,10,15,15,13,19,19,19,19
s
    
SyntaxError: '{' was never closed
s= {80,70,24,14,12,15,10,101,10,10,15,15,13,19,19,19,19}
    
s
    
{101, 70, 10, 12, 13, 14, 15, 80, 19, 24}
id(s)
    
2382828708224
a={1,12.3,"str"}
    
a
    
{'str', 1, 12.3}
set(s)
    
{101, 70, 10, 12, 13, 14, 15, 80, 19, 24}
type(s)
    
<class 'set'>
d = {'productname':'XYZ','PRICE':999,'stock':True
     d
...      
SyntaxError: '{' was never closed
>>> d = {'productname':'XYZ','PRICE':999,'stock':True}
...      
>>> d
...      
{'productname': 'XYZ', 'PRICE': 999, 'stock': True}
>>> 
>>> d
...      
{'productname': 'XYZ', 'PRICE': 999, 'stock': True}
>>> s={1,2,3,4}
...      
>>> s = frozenset({1,2,3,4,10})
...      
>>> a = True
...      
>>> a =True
...      
>>> b =False
...      
>>> type(a)
...      
<class 'bool'>
>>> a={}
...      
>>> l=[]
...      
>>> t=()
...      
>>> s=''
...      
>>> s = None
...      
>>> s
...      
>>> type(s)
...      
<class 'NoneType'>
