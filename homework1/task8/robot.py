class Robot:
    def __init__(self, battery):
        self.battery = battery

    def move(self):
        b = self.battery
        if b >= 10:
            print(f'{b - 10}%')
        else:
            print('Робот разряжен')
