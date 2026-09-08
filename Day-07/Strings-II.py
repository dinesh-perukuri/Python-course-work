Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Continuetion of strings
#Whitespace & Trimming
#Trimming
s = '      Hello       world     '
s.strip()
'Hello       world'
s.rstrip()
'      Hello       world'
s.lstrip()
'Hello       world     '
#Replace
s.replace(' ','')
'Helloworld'


#Splitting & Joining methods
s = 'java-python-flask-mysql-fastapi-c'
s.split('-',2)
['java', 'python', 'flask-mysql-fastapi-c']

s.rsplit('-',2)
['java-python-flask-mysql', 'fastapi', 'c']
s.lsplit('-',2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.lsplit('-',2)
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
l = '''pyton
java
mysql
flask
'''
l
'pyton\njava\nmysql\nflask\n'
l.splitlines()
['pyton', 'java', 'mysql', 'flask']
c = ['python', 'java', 'mysql', 'flask']
c
['python', 'java', 'mysql', 'flask']
''.join(c)
'pythonjavamysqlflask'
' '.join(c)
'python java mysql flask'
'      '.join(c)
'python      java      mysql      flask'
' ,'.join(c)
'python ,java ,mysql ,flask'
', '.join(c)
'python, java, mysql, flask'
'@'.join(c)
'python@java@mysql@flask'
'@, '.join.(c)
SyntaxError: invalid syntax
'@, '.join.(c)
'@, '.join(c)
SyntaxError: invalid syntax
'@, '.join(c)
'python@, java@, mysql@, flask'
'-'.join(('1','2','3'))
'1-2-3'
'-'.join({'1','2','3'})
'3-1-2'
#Partiation
a = 'strings.py'
a,partiation('.')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a,partiation('.')
NameError: name 'partiation' is not defined
a.partiation('.')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.partiation('.')
AttributeError: 'str' object has no attribute 'partiation'. Did you mean: 'partition'?
a.partition('.')
('strings', '.', 'py')
a = 'string.py.java.png.txt'
a
'string.py.java.png.txt'
a.partition('.')
('string', '.', 'py.java.png.txt')
a.rpartition('.')
('string.py.java.png', '.', 'txt')
#String testing method
#Starts with
a.startswith('str')
True
a.startswith('list')
False
#Ends with
a.endswith('py.')
False
a.endswith('.png')
False
a = 'string.png'
a.startswith('str')
True
a.startswith('list')
False
a.endswith('py.')
False
a.endswith('.png')
True
>>> #starts and ends included in ^^^
>>> #islower
>>> 'pythonv.13',islower()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    'pythonv.13',islower()
NameError: name 'islower' is not defined
>>> 'pythonv.13'.islower()
True
>>> 'PYTHON234567@$%^&*'.isupper()
True
>>> 'estuy'.isalpha()
True
>>> 'fvkgnek;jnwegf;kjgnwb'isalnum
SyntaxError: invalid syntax
>>> 'fvkgnek;jnwegf;kjgnwb'.isalnum()
False
>>> 'hfshehefjgejew'.isalnum()
True
>>> '123456789'.isalnum()
True
>>> '     '.isspace()
True
>>> '     Hello;'.isspace()
False
>>> #Title
>>> 'Hlo Wor'.istitle()
True
>>> 'HLOWORLD'.istitle()
False
>>> #Identifier
>>> 'my__var'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> #Is decimal, Is digit, Is numeric
>>> #Is numeric can get numeric arabic and roman numbers
>>> '122563'.isdecimal()
True
>>> 'DSHVBRIJBNRJG'.isdecimal()
False
>>> '955215'.isdigit()
True
>>> '5655'.isnumeric()
True
>>> '687+651'isnumeric()
SyntaxError: invalid syntax
>>> '687+651'.isnumeric()
False
