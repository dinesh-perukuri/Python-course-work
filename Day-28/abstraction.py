from abc import ABC,abstractmethod

class Payment(ABC):
    def source(self):
        print("Scanner/upiid/mobile number")
    def amount(self):
        print("Enter the amount")
    def bank(self):
        print("Select the Bank")
    def pin(self):
        print("Enter the pin")

    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment Success/fail")

class kotak(Payment):
    def paymentprocess(self):
        print("Payment is process through kotak Bank")

class Axis(Payment):
    def paymentprocess(self):
        print("Payment is process through Axis Bank")

class PUB(Payment):
    def paymentprocess(self):
        print("Payment is process through PUB Bank")

class ICICI(Payment):
    def paymentprocess(self):
        print("Payment is process through ICICI Bank")

Dinesh = kotak()
Dinesh.source()
Dinesh.amount()
Dinesh.bank()
Dinesh.pin()
Dinesh.paymentprocess()
Dinesh.paymentstatus()

Rasool = Axis()
Rasool.source()
Rasool.amount()
Rasool.bank()
Rasool.pin()
Rasool.paymentprocess()
Rasool.paymentstatus()

Ranjith = PUB()
Ranjith.source()
Ranjith.amount()
Ranjith.bank()
Ranjith.pin()
Ranjith.paymentprocess()
Ranjith.paymentstatus()

Bobby = ICICI()
Bobby.source()
Bobby.amount()
Bobby.bank()
Bobby.pin()
Bobby.paymentprocess()
Bobby.paymentstatus()