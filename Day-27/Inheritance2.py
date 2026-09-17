'''
class Whatsapp1:
    def status(self):
        print('You can share the status for 24hrs')
class Whatsapp2(Whatsapp1):
    def status(self):
        super().status()                                        #SUPER 
        print('You can add the music and You can react ')

a=Whatsapp2()
a.status()
'''
class Instagram1:
    def status(self):
        print('You can share the story for 24hrs')
class Instagram2:
    def status(self):                                      
        print('You can add the music and You can react ')
class Instagram3(Instagram1,Instagram2):
    def status(self):
        Instagram1.status(self)
        Instagram2.status(self)
        print('You can add cross platform')

a=Instagram3()
a.status()