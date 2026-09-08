'''
def functionname(arg):
    #statements
    return (opt)

functionnname(para)
'''

'''
def gst(price):
    print("Original Price:",price)
    print("Final Price:",price+price*0.18)
gst(1000)
gst(5800)
gst(3620)
gst(5471)
gst(50000)
'''

'''
def table(n):
    print(f"{n}-Table")
    print('--------------------')
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

for i in range(1,21):
    table(i)
    '''

'''
def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap Year"
    else:
         return "Not a Leap Year"
print(isleap(2012))
print(isleap(2020))
print(isleap(2026))
'''

'''
def ifprime(number):
    if number%2==0 or (number%10==0) and (number%250!=0):
        return "Prime number"
    else:
        return "Not a prime number"
print(ifprime(2-11))
print(ifprime(4-18))
print(ifprime(10-15))
print(ifprime(10-20))
'''
#Types of arguments there are 4 types of arguments :-
#positional 
#Keyword
#Default
#Variable length

#  Positional
'''
def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd",pwd)
display('Dinesh','dperukuri@gmail.com','Dinesh$5567')
display('dperukuri@gmail.com','Dinesh','Dinesh$5567')
display('Dinesh$5567','Dinesh','dperukuri@gmail.com')
'''
#Keyword 
'''
def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd",pwd)
display(name='Dinesh',email='dperukuri@gmail.com',pwd='Dinesh$5567')
display(email='dperukuri@gmail.com',name='Dinesh',pwd='Dinesh$5567')
display(pwd='Dinesh$5567',name='Dinesh',email='dperukuri@gmail.com')
'''

#Default
'''
def display(name,email,pwd=None):
    print("name:",name)
    print("email",email)
    print("pwd",pwd)
display("Dinesh","email")
display("Dinesh","email","pwd@123")
'''

# Variable length
'''
def display(*names):
    print(names)
display("Dinesh")
display("Dinesh","Abhi")
display("Dinesh","Sowmya","Abhi")
display("Dinesh","Sowmya","Abhi","Vikky")
'''
#keys ascii
'''
def display(**names):
    print(names)
display(n1="Dinesh")
display(n1="Dinesh",n2="Abhi",n3="Sowmya")
'''
