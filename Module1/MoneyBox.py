class MoneyBox:

    def __init__(self, capacity): # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.money = 0

    def can_add(self, v): # True, если можно добавить v монет, False иначе
        return self.capacity - self.money >= v

    def add(self, v): # положить v монет в копилку
        self.money += v
