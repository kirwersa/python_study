from cardpayment import CardPayment
from cahspayment import CashPayment


def main():
    card_pay = CardPayment()
    card_pay.pay(10)

    cash_pay = CashPayment()
    cash_pay.pay(55)


if __name__ == '__main__':
    main()
