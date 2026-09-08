Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=12.9
>>> c='dinesh'
>>> print(a,b,c)
10 12.9 dinesh
>>> print("a",a,"b",b,"c",c)
a 10 b 12.9 c dinesh
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 12.9 c= dinesh
>>> print("a=",a,"b",b,"c",c,sep='')
a=10b12.9cdinesh
>>> print("a=",a,"b",b,"c",c,sep='\n')
a=
10
b
12.9
c
dinesh
>>> print("a",a,"b",b,"c",c,sep='\t')
a	10	b	12.9	c	dinesh
>>> print("a",a,"b",b,"c",c,sep='\t',end='\n\n')
a	10	b	12.9	c	dinesh

>>> print("a",a,"b",b,"c",c,sep='\t',end='@')
a	10	b	12.9	c	dinesh@
>>> #recomended f string
>>> print(f'a={a} b={b} c={c}')
a=10 b=12.9 c=dinesh
>>> #Not recomended but uses in c++ java
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=12.900000 c=dinesh
>>> print('a{} b={} c={}'.format(a,b,c))
a10 b=12.9 c=dinesh
>>> print('a{} b={} c={}'.format(c,a,b))
adinesh b=10 c=12.9
>>> print('a={} b={} c={}'.format(c,a,b))
a=dinesh b=10 c=12.9
print('a={0} b={1} c={2}'.format(c,a,b))
a=dinesh b=10 c=12.9
print('a={2} b={0} c={1}'.format(c,a,b)).
SyntaxError: invalid syntax
print('a={2} b={0} c={1}'.format(c,a,b))
a=12.9 b=dinesh c=10
