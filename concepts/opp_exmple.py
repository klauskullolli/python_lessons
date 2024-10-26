# this is a class that define a Car ide
class Car:

    nr_cars = 1

    def __init__(self, model, engine) -> None:
        self.model = model
        self.engine = engine


class Phone:
    counter = 0

    def __init__(self) -> None:
        Phone.counter += 1


class MobilePhone(Phone):
    last_device = 0

    def __init__(self, model) -> None:
        super().__init__()
        MobilePhone.last_device += 1
        self.model = model





class SmartPhone(MobilePhone):
    last_device = 0

    def __init__(self, model, memory) -> None:
        super().__init__(model)
        self.memory = memory
        SmartPhone.last_device += 1



if __name__ == "__main__":

    # c1 = Car(model="mercedes", engine=2.2)

    # print(Car.__dict__)
    # print(c1.__dict__)
    m1 = MobilePhone("samsung")
    s1 = SmartPhone(model="samsung", memory=256)

    print("device_number: ", m1.last_device)
    print("device_number: ", s1.last_device)
    print(s1.__dir__())
