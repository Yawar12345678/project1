class PowerOfTwo:
    def __init__(self, max):
        self._max = max

    def __iter__(self):
        self._index = 0
        return self
    def __next__(self):
        if self._index > self._max:
            raise StopIteration
        self._index += 1
        return 1

Pot = PowerOfTwo(5)
for i in Pot:
    print(i)
