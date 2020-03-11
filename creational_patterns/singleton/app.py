class MyClass:
    _instance = None
    some_var = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super().__new__(cls)
            # Put any initialization here
        return cls._instance


if __name__ == '__main__':
    mc = MyClass()
    mc1 = MyClass()
    print(mc is mc1)
    mc.some_var = 'hello'
    print(mc.some_var)
    print(mc1.some_var)