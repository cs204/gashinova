class jar:
    @property
    def capacity(self):
        return self._capacity

        @capasity.setter
        def capacity(self, capacity):
            if not (capacity >=0 and type(capacity)is int):
                raise ValueError("wrong capacity")
            self._capacity = capasity

jar=jar()
jar.capacity = 13
print("\N{Cookie}"*3)
print(type(3)is int)
