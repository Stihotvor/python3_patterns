from python_specific_patterns.sentinel_object_pattern.pattern_objects import NullObject


def foo(name: str = NullObject):
    if name is not NullObject:
        print(name)


if __name__ == '__main__':
    foo()
    foo(name='Jack')
