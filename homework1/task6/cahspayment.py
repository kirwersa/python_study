from ipayment import IPayment


class CashPayment(IPayment):
    def __init__(self, amound):
        super().__init__(amound)

    def pay(self, amound):
        print(f'Оплата наличными {amound}$.')

    def refund(self, amound):
        print(f'Сдача {amound}$.')
