
class Mat2():

    matrix: list

    def __init__(self, row1: list, row2: list):
        self.matrix = []
        self.matrix.append(row1)
        self.matrix.append(row2)

    def __add__(self, m: 'Mat2'):
        for i in [0, 1]:
            for j in [0, 1]:
                self.matrix[i][j] = self.matrix[i][j] + m.matrix[i][j]
        return self

    def __mul__(self, other: int):
        for i in [0, 1]:
            for k in [0, 1]:
                self.matrix[i][k] = self.matrix[i][k] * other
        return self

    def __str__(self):
        return f"{[x for x in self.matrix[0]]}\n{[x for x in self.matrix[1]]}"
