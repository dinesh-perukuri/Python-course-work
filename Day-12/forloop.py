# String list tuple set dict range 

#string 
s = 'python programming'
for i in s:
    print(i)

l = [1, 2, 3, 4, 5]
for num in l:
    print(num)

prices = (9845,4578,2577)
for price in prices:
    print(price)

names = {'Dinesh', 'Ramesh', 'Suresh'}
for name in names:
    print(name)

d = {1:2,2:4,3:6,4:8,5:10}
for i in d:
    print(i, d[i])

# Range gives numeric values

range(start,end+1,step):(0,1)
for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(5,0,-1):
    print(i)

#Index of the value using range function i value gives numeric in range function and i value is used to get the index of the value in the list
s = 'python programming'
for i in range(len(s)):
    print(i, s[i])

s = [2566,9585154,32656454,654654,654654,654654]
for i in range(len(s)):
    print(i, s[i])  
  # set and dict are not indexable so we cannot use range function to get the index of the value in set and dict ^^^


#Enumarate give the values and original index of the value in the list and duplicates won't allow to get the index of the value in the list

s = [1546,1564,2549,2547,]
for i in enumerate(s):
    print(i[0],i[1])


d = {1:2,2:4,3:6,4:8,5:10}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])

#Jmping statements are two types 'Break' and 'Continue'

for i in range(1,11):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i == 5:
        continue
    print(i)

#forwithelse statement is used to check the condition in the for loop if the condition is true then it will execute the else statement if the condition is false then it will not execute the else statement
l = [12,13,15,16,17,18,19]
n=26
for i in l:
    if i == n:
        print('Found')
        break
else:
    print('Not Found')


for i in range(1,11):
    if i == 15:
      break
    print(i)
else:
    print('End of the loop')

pin = 1234
for i in range(5):
    epin = int(input('Enter the pin: '))
    if epin == pin:
        print('Unlock phone')
        break
    else:
        print("Invalid pin")
else:
    print('Try after 30 seconds')


prime = int(input('Enter the number: '))
for i in range(2,prime):
    if prime % i == 0:
        print('Not a prime number')
        break
else:
    print('Prime number')


n = 14
for i in range(2,n//2+1):
    if n % i == 0:
        print('Not a prime number')
        break
else:
    print('Prime number')



