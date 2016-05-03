class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, num):
        if num > 0:
            super().append(num)
        else:
            raise NonPositiveError

a = PositiveList()
a.append(2)
a.append(0)
