class Car:
    """A simple example class"""
    i = 12345

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        # returns a string that can be fed to eval() to get
        # back the original object, obj == eval(repr(obj))
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mileage!r})')

    def __str__(self):
        return f'a {self.color} car'

    def f(self):
        return 'hello world'


# Valid attributes of Car
print (Car.i)
print (Car.f)
print (Car.__doc__)

x = Car("blue", 1234)   # Instantiate
print (x)               # this will call Car.__str__
print (repr(x))         # this will call Car.__repr__
