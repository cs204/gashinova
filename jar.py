class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self.total = 0

    def __str__(self):
        return ("🍪" * self.total)

    def deposit(self, n):
        self.total = self.total + n

    def withdraw(self, n):
        self.total = self.total - n

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity < 0 or isinstance(capacity, int) == False:
            raise ValueError
        else:
            self.__capacity = capacity

    @property
    def size(self):
        return self.total
