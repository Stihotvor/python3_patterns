class Note:
    def __init__(self, fraction):
        self.fraction = fraction

    def clone(self):
        return Note(self.fraction)


class Sharp:
    def clone(self):
        return Sharp()


class Flat:
    def clone(self):
        return Flat()
