Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = 10
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c = 10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> swap the value delete the value
SyntaxError: invalid syntax
>>> swapthevaluedeletethevalue
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    swapthevaluedeletethevalue
NameError: name 'swapthevaluedeletethevalue' is not defined
>>> a,b b,a
SyntaxError: invalid syntax
>>> a,b = b,a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
10
>>> c
30
>>> d
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> del c
>>> c
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    c
NameError: name 'c' is not defined
b
10
del b
b
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    b
NameError: name 'b' is not defined
