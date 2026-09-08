Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Input formatting
>>> #int float complex str list tuple set dict bool
>>> a = input()
codegnan
>>> a
'codegnan'
>>> a = input()
1234
>>> a
'1234'
>>> a  = input("Enter the value:")
Enter the value:Abhi@1235
>>> a
'Abhi@1235'
>>> marks = input("Enter the marks:")
Enter the marks:800
>>> marks
'800'
>>> price = float(input("Enter the price:"))
Enter the price:999
>>> price
999.0
>>> marks = int(input("Enter the marks"))
Enter the marks 1000
>>> marks
1000
>>> cgpa = float(input("Enter the cgpa:"))
Enter the cgpa:99.8
>>> cgpa
99.8
>>> #.Split
>>> #.Split list of strings
>>> #.Spli0t & list of strings
>>> names.split()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    names.split()
NameError: name 'names' is not defined
>>> names = (Abhi,games,ETS)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    names = (Abhi,games,ETS)
NameError: name 'Abhi' is not defined
>>> names = ('Abhi,games,ETS')
>>> names.split
<built-in method split of str object at 0x0000020B1ECD7730>
>>> names
'Abhi,games,ETS'
names.split
<built-in method split of str object at 0x0000020B1ECD7730>
names.split(',')
['Abhi', 'games', 'ETS']
courses = 'python,java,c++,flask'
courses
'python,java,c++,flask'
courses.split
<built-in method split of str object at 0x0000020B1ECD7D70>
courses.split(',')
['python', 'java', 'c++', 'flask']
softskills = 'communication quicklearner'
softskills
'communication quicklearner'
softskills(',')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    softskills(',')
TypeError: 'str' object is not callable
softskills.split()
['communication', 'quicklearner']
softskills.split(',')
['communication quicklearner']
['communication quicklearner']
['communication quicklearner']
names = input('Enter the names:').split()
Enter the names:Abhi ets games
names
['Abhi', 'ets', 'games']
names = tuple(input("Enter the names:").split())
Enter the names:Abhi ets games
names
('Abhi', 'ets', 'games')
names = set(input("Enter the names:").split())
Enter the names:abhi ets martin 
names
{'ets', 'martin', 'abhi'}
#List of integers
#List of integers
#Maps uses to iterate the vlue
#Float to replace the value
marks = value().split()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    marks = value().split()
NameError: name 'value' is not defined. Did you mean: 'False'?
marks=('11,22,33,44,55')
marks
'11,22,33,44,55'
marks=input().split()
11 22 33 44 55
marks
['11', '22', '33', '44', '55']
map(int,marks)
<map object at 0x0000020B1ECD7A00>
list(map(int,marks))
[11, 22, 33, 44, 55]
marks=list(map(int,input("Enter the marks").split()))
Enter the marks11 22 33 44 55
marks
[11, 22, 33, 44, 55]
marks=tuple(map(int,input("Enter the marks").split()))
Enter the marks11 22 33 44 55
marks
(11, 22, 33, 44, 55)
marks=set(map(int,input("Enter the marks")()))
Enter the marks44 55 77 88 99
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    marks=set(map(int,input("Enter the marks")()))
TypeError: 'str' object is not callable
marks
(11, 22, 33, 44, 55)
marks=set(map(int,input("Enter the marks").split()))
Enter the marks44 55 77 88 99
marks
{99, 44, 77, 55, 88}
marks=set(map(float,input("Enter the marks").split()))
Enter the marks999999999999999
marks
{999999999999999.0}
marks=bool(map(float,input("Enter the marks").split()))
Enter the marks22 55 99 77 
marks
True
marks
True
marks=complex(map(float,input("Enter the marks").split()))
Enter the marks55 44 77 88 99 
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    marks=complex(map(float,input("Enter the marks").split()))
TypeError: complex() argument must be a string or a number, not map
marks
True
#Packinng and unpacking
#Packing and unpacking
a,b=[1,2]
a
1
b
2
a,b,c=(1,12.3,"str")
a
1
b
12.3
c
'str'
email,password=input("Enter the email,password:").split()
Enter the email,password:dperukuri@gmail.com,Dinesh$22222
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    email,password=input("Enter the email,password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
Enter the email,password:dperukuri@gmail.com Dinesh$22222
SyntaxError: invalid syntax
Enter the email,password: dperukuri@gmail.com Dinesh222223
SyntaxError: invalid syntax
email,password=input("Enter the email,password:").split()
Enter the email,password:dinesh@1234 polo345
email
'dinesh@1234'
password
'polo345'
name,marks=input("Enter the name and marks:").split()
Enter the name and marks:99
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    name,marks=input("Enter the name and marks:").split()
ValueError: not enough values to unpack (expected 2, got 1)

name dileep marks 99
SyntaxError: invalid syntax
name,marks=input("Enter the name and marks:").split()
Enter the name and marks:abhi 68
name
'abhi'
marks
'68'
int(marks)
68
a,b,c=list(map(int,input().split()))
55 22 88
a
55
b
22
c
88
#Eval function for the boolen value only
status=eval(input())
True
status
True
type(status)
<class 'bool'>
status=eval(input())
2+3j
status
(2+3j)
type(status)
<class 'complex'>
status=eval(input())
1400
status
1400
status=eval(input())
[1,2,3,5]
SyntaxError: multiple statements found while compiling a single statement
status=eval(input())
[1,2,3,5]
status
[1, 2, 3, 5]
status=eval(input())
(8,9,5,7,)
status
(8, 9, 5, 7)
status=eval(input())
{1:1,2:2,3:3,4:4,5:5}
status
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
type(status)
<class 'dict'>
