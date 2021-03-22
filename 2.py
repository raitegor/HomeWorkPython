class Road:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def weight (self, mass, thick):
        print(f'Масса асфальта для покрытия всей дороги: {(self.length * self.width * mass * thick)/1000} тонн')

massa_1 = Road(10,1000)
massa_1.weight(25, 5)