import re

from global_object_pattern.validators import magic_check
from tools.time import timing


# Pre-calculated computation
@timing
def foo_01():
    for i in range(1000):
        magic_check.findall('*hello')


# On sight computation
@timing
def foo_02():
    for i in range(1000):
        re.compile('([*?[])').findall('*hello')


if __name__ == '__main__':
    foo_01()
    foo_02()