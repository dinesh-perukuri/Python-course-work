'''
try:
    print(10/10)
except ZeroDivisionError:
    print("Unable to divide a number with zero")
else:
    print("No errors")
finally:
    print("End of the program")
'''

'''
try:
    d={1:1,2:2,3:3}
    #print(d[4])
    l = [1,2,3,4]
    #print(l[5])
    #print('a+7')
    #a = int(input("Enter the amount: ")) #
    #print(n)
    print(10/10)

except NameError:
    print("Var is not defined")
except ValueError:
    print("Enter the proper value")
except TypeError:
    print("Use same datatypes")
except IndexError:
    print("Index is out of range")
except KeyError:
    print("Key is not present")
except ZeroDivisionError:
    print("Unable to divide a number with zero")
else:
    print("No errors")
finally:
    print("End of the program")
'''


'''
except (NameError,ValueError,TypeError,IndexError,KeyError,ZeroDivisionError) as e
    print("Error Occured:",e)

else:
     print("No errors")
finally:
    print("End of the program")
'''

'''
try:
    amount = int(input("Enter the amount: "))
    if amount < 0:
        raise Exception("Amount needs to be greater then 0")
except Exception as e:
    print("Error Occured:",e)
else:
    print("No errors")
finally:
    print("End of the program")
'''