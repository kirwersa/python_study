from ipayment import IPayment


class CardPayment(IPayment):

    def pay(self, amount):
        print(f"pay {amount}")

    def refund(self, amount):
        print(f"refund {amount}")
