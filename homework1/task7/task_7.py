from emailnotifier import EmailNotifier
from smsnotifier import SMSNotifier


def main():

    email = EmailNotifier()
    email.send("hello")

    sms = SMSNotifier()
    sms.send('hi')


if __name__ == '__main__':
    main()
