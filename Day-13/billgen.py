'''
data = {'katana' : 10000,
    'bracelet' : 1000,
    'comic' : 899,
    'code of japan' : 1200,
    'og shirt' : 5000,
    'car' : 50000,
    'mazda' : 952000,
    'bazuka' : 45820,
    'milliem' : 250003,}
for i in data:
    print(i.ljust(20),data[i])

prods = input("Enter the products:").split()
print(prods)
'''

'''
data = {'katana' : 10000,
    'bracelet' : 1000,
    'comic' : 899,
    'code of japan' : 1200,
    'og shirt' : 5000,
    'car' : 50000,
    'mazda' : 952000,
    'bazuka' : 45820,
    'milliem' : 250003,}
for i in data:
    print(i.ljust(20),data[i])

prods = input("Enter the products:").split()
print("##########Bill##########")
bill = 0
for i in prods:
    print(i.ljust(20),data[i])
    bill += data[i]
    print("Total bill".ljust(20), bill) 
'''

bill = 0
while True:
    product = input("Enter the product name or [E]xit: ")
    if product == 'E' or product == 'e':
        print("Thanks for shopping")
        print("Total bill:",bill)
        break
    else:
        quantity = int(input("Enter the quantity:"))
        bill += data[product]*quantity