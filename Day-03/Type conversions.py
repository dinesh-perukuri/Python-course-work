Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
float = 13.4
f
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    f
NameError: name 'f' is not defined
tuple(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
f = 13.4
int(f)
13
complex(f)
(13.4+0j)
str(f)
'13.4'
cool(f)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    cool(f)
NameError: name 'cool' is not defined. Did you mean: 'bool'?
bool(f)
True
str(c)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    str(c)
NameError: name 'c' is not defined
bool(c)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    bool(c)
NameError: name 'c' is not defined
bool(f)
True
c = 12.36+96p
SyntaxError: invalid decimal literal
c = 12.36+9p
SyntaxError: invalid decimal literal
c = 12+6j
int(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
str(c)
'(12+6j)'
bool(c)
True
complec(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    complec(c)
NameError: name 'complec' is not defined. Did you mean: 'complex'?
complex(c)
(12+6j)
s = '901048'
a = 'codegnan'
int(a)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'codegnan'
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'codegnan'
>>> int(s)
901048
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float(s)
TypeError: 'float' object is not callable
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float(a)
TypeError: 'float' object is not callable
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    complex(a)
ValueError: complex() arg is a malformed string
>>> complex(s)
(901048+0j)
>>> bool(s)
True
>>> list(s)
['9', '0', '1', '0', '4', '8']
>>> tuple(s)
('9', '0', '1', '0', '4', '8')
>>> set(s)
{'8', '0', '1', '4', '9'}
>>> list(a)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
>>> ['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
>>> 
