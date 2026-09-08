'''
fa = 
eval(input("Follows the account:"))
if fa:
    print("You are following the account.")
    cf = eval(input("close friend":))
    if cf: 
        print("You are a close friend.")                                                                                              
    else:
        print("You are not a close friend.")
'''


'''
reg = eval(input("egistered:"))
if reg:
    fee = eval(input("Fee paid:"))
    if fee:
        print("Tournment Entry Confirmed")
    else:
        print("Entry Fee pending")
else:
    print("You are not registered for the tournment.")
                   '''


data = {
    'Dinesh':{'status':True,'python':95,'mysql':90,'flask':85},
    'Alice':{'status':False,'python':95,'mysql':90,'flask':75},
    'Bobby':{'status':True,'python':None,'mysql':None,'flask':None},
    'vijay':{'status':True,'python':75,'mysql':70,'flask':65},    
}
name = input("Enter the name:")
if name in data:
    if data[name]['status']:
        sum = data[name]['python'] + data[name]['mysql'] + data[name]['flask']
        avg = sum/3
        print(f"Hello {name}!!!")
        print(f"Your average score is {avg}")
        if avg >= 90:
            print(f"Outstanding performance")
        elif avg >= 80:
            print(f"Good performance")  
        elif avg >= 70:
            print(f"Average performance")
        else:
            print(f"Poor performance")
    else:
        print(f'{name} Lag gai guruu')
       





