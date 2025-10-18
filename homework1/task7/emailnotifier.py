from inotifier import INotifier


class EmailNotifier(INotifier):
    def send(self, email):
        print(f'Вам пришло сообщение {email}')
