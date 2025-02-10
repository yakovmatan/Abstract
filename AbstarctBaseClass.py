from abc import ABC, abstractmethod
import math
# מחלקת צורות
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



class Rectangle(Shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi



#מחלקת תשלום
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self,payment_sum):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self,payment_sum):
        print(f"payment out {payment_sum} was made using a credit card")


credit_card = CreditCardProcessor()
credit_card.process_payment(100)