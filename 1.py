class Matrix:
    def __init__(self, p_1):
        self.p_1 = p_1

    def __add__(self, other):
        c = []
        for i in range(len(self.p_1)):
            c.append([])
            for j in range(len(self.p_1[0])):
                MyClass(c[i].append(self.p_1[i][j] + other.p_1[i][j]))
        return c

    def __str__(self):
        return f'Параметры объекта {self.p_1}'


a = [[12, 19, 45], [90, 34, 55], [45, 78, 66]]
b = [[13, 19, 23], [72, 5, 13], [95, 71, 90]]

one = Matrix(a)
two = Matrix(b)
print(one + two)