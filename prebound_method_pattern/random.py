from datetime import datetime


class RandomB:
    def __init__(self):
        self.set_seed(datetime.now().microsecond % 255 + 1)

    def set_seed(self, value):
        self.seed = value

    def random(self):
        self.seed, carry = divmod(self.seed, 2)
        if carry:
            self.seed ^= 0xb8
        return self.seed


# Create own module class instance
_instance = RandomB()

# Bound internals to a module namespace
random = _instance.random
set_seed = _instance.set_seed
