'''
file = open("C:/Users/DINESH/Desktop/python-course-work/Day-30/demo.txt",'r')
print(file.read())
file.seek(0)
print(file.readlines())
file.seek(0)
print(file.readlines())
file.close()
'''

'''
with open("C:/Users/DINESH/Desktop/python-course-work/Day-30/demo.txt",'r') as file:
    print(file.read())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    print(file.readlines())
    file.close()
    '''

'''
with open("C:/Users/DINESH/Desktop/python-course-work/Day-30/demo.txt",'w') as file:
     file.write("hello world")
'''

'''
with open("C:/Users/DINESH/Desktop/python-course-work/Day-30/demo.txt",'a') as file:
     file.write("hello world")
'''

with open("C:/Users/DINESH/Desktop/python-course-work/Day-30/demo.txt",'a+') as file:
     file.write("\nfile operations")
     file.seek(0)
     print(file.read())