from constant_patters.variables import FOO_02_RESULT
from tools.time import timing


# Function with local calculations
@timing
def foo_01():
    for i in range(1000):
        x = 1000/56*10


# Function with pre-calculated data
@timing
def foo_02():
    for i in range(1000):
        x = FOO_02_RESULT


if __name__ == '__main__':
    foo_01()
    foo_02()

