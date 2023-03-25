def add(*args):
    for i in args:
        return sum(args)


print(add(10,10,15,5))

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(model="Red", make="Tesla")
print(my_car.model, my_car.make)
