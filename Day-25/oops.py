'''
class Fancode:
    pass
Dinesh = Fancode()
Ranjith = Fancode()
Rasool = Fancode()
dipak = Fancode()
'''

'''
class Fancode:
    discount = 88
    def info(self,name,phoneno,address):
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print(f'Welcome to the Fancode page',self.name)

Dinesh = Fancode()
Dinesh.info('Dinesh',9618535842,'Hyd')
Ranjith = Fancode()
Ranjith.info('Ranjith',9618535862,'Zym')
Rasool = Fancode()
Rasool.info('Rasool',9618535862,'Pak')
dipak = Fancode()
dipak.info('dipak',9618535862,'Mars')
'''

'''
class Fancode:
    discount = 88
    @classmethod
    def updatdiscount(cls):
        cls.discount = 98
        print("Updated Discount:",cls.discount)

    def info(self,name,phoneno,address):
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print(f'Welcome to the Fancode page',self.name)

    @staticmethod
    def banner():
        print(f"{Fancode.discount}% Aareaa ahaa reaa discount lekeaa jareaa ")


Dinesh = Fancode()
Dinesh.info('Dinesh',9618535842,'Hyd')
Dinesh.updatdiscount()
Dinesh.banner()
Ranjith = Fancode()
Ranjith.info('Ranjith',9618535862,'Zym')
Ranjith.updatdiscount()
Ranjith.banner()
Rasool = Fancode()
Rasool.info('Rasool',9618535862,'Pak')
Rasool.updatdiscount()
Rasool.banner()
dipak = Fancode()
dipak.info('dipak',9618535862,'Mars')
dipak.updatdiscount()
dipak.banner()
'''
