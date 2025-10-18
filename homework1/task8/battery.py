class Battery:
    def __init__(self, level: int):
        self.levle = level

    def move(self):
        h = self.levle
        if h >= 10:
            print(f'{h - 10}%')
        else:
            print('Устройство разряжено')
