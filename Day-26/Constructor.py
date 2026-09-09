'''
class F1:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f"Welcome to F1, {self,username}")

Dinesh = F1('Dinesh','96584712')
'''
'''
class F1:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self.__post = []

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self.__post

Dinesh = F1('Dinesh','96584712')

print(Dinesh.username)
print(Dinesh.getpassword())
print(Dinesh.accesspost)
'''
'''
class F1:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):

        Dinesh.username = 'Dinesh@123'
        return self._post
        print(Dinesh.username)


    @accesspost.setter
    def accesspost(self,newpost):
        self.post.append(newpost)

Dinesh = F1('Dinesh','96584712')

print(Dinesh.username)
print(Dinesh.getpassword())
print(Dinesh.accesspost)

Dinesh.username = 'Dinesh@123'
print(Dinesh.username)

Dinesh.setpassword('Dinesh1234')
print(Dinesh.getpassword())

Dinesh.accesspost = 'Python Intro'
Dinesh.accesspost = 'Strings'
Dinesh.accesspost = 'project'
print(Dinesh.accesspost)
'''