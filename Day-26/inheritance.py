'''
class whatsappv1:
    def message(self):
        print("Youcan send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status foe 24hrs")

Dinesh = whatsappv1()
Dinesh.message()

Rasool = whatsappv2()
Rasool.status()
'''
'''
class whatsappv1:
    def message(self):
        print("Youcan send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status foe 24hrs")

class whatsappv3(whatsappv2):
    def groups(self):
        print("You can create group and talk with multiple people")

Dinesh = whatsappv1()
Dinesh.message()

Rasool = whatsappv2()
Rasool.status()

Ranjith = whatsappv3()
Ranjith.message()
Ranjith.status()
Ranjith.groups() 
'''

