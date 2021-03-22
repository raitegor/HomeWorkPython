import time
class TrafficLight:
    def __init__(self, *c):
        self._color = c
    def running(self):
        print(f'Стой! горит красный {self._color[0]}')
        time.sleep(7)
        print(f'Будь готов к пути, горит {self._color[1]}')
        time.sleep(2)
        print(f'Можно мчатЬ! Горит {self._color[2]}')
        time.sleep(5)
        print(f'Мы проехали светофор!')

trafic = TrafficLight('Красный', 'Желтый', 'Зеленый')
trafic.running()
