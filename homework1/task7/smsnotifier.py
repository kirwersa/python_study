from inotifier import INotifier


class SMSNotifier(INotifier):
    def send(self, SMS):
        print(f'Вам пришло сообщение {SMS}')
