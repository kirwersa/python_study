from cpu import CPU
from ram import RAM


class Computer():

    def __init__(self, model, size):
        self.cpu = CPU(model)
        self.ram = RAM(size)

    def run(self):
        print(f"compute on {self.cpu.model} using {self.ram.size_gb} GB")
