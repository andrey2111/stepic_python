class Buffer:
    def __init__(self): # конструктор без аргументов
        self.buffer = []

    def add(self, *a): # добавить следующую часть последовательности
        for i in a:
            self.buffer.append(i)
            if len(self.buffer) == 5:
                print(sum(self.buffer))
                self.buffer = []

    def get_current_part(self): # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.buffer

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]


a = dict()
a["key"] = 'value'
print(a)
