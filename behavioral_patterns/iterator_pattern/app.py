class OddNumbers:
    "An iterable object"

    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        return OddIterator(self)


class OddIterator:
    "An iterator"

    def __init__(self, container):
        self.container = container
        self.n = -1

    def __next__(self):
        self.n += 2
        if self.n > self.container.maximum:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self


numbers = OddNumbers(7)
for n in numbers:
    print(n)


it = iter(OddNumbers(5))
print(next(it))
print(next(it))

print(list(numbers))
print(set(n for n in numbers if n > 4))
