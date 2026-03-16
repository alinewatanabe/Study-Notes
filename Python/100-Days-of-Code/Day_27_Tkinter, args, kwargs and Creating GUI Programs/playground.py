def add(*args):
    S = 0
    for i in args:
        S += i
    return S


print(add(1, 2, 3, 4))

def calculator(n,**kargs):
    # for key, value in kargs.items()
    #     print(key)
    n += kargs["add"]
    n *= kargs["multiply"]
    print(n)

calculator(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw["model"]
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

myCar = Car(model="GT-R", colour="black")
print(myCar.make)
print(myCar.model)
print(myCar.colour)