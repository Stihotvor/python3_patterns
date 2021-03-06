class Grade(object):
    _instances = {}

    def __new__(cls, percent):
        percent = max(50, min(99, percent))
        letter = 'FDCBA'[(percent - 50) // 10]
        self = cls._instances.get(letter)
        if self is None:
            self = cls._instances[letter] = object.__new__(Grade)
            self.letter = letter
        return self

    def __repr__(self):
        return 'Grade {!r}'.format(self.letter)


print(Grade(55), Grade(85), Grade(95), Grade(100))
print(len(Grade._instances))    # number of instances
print(Grade(95) is Grade(100))  # ask for ‘A’ two more times
print(len(Grade._instances))    # number stayed the same?