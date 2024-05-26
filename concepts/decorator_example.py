from typing import Any


def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> The whole order would be packed with',
                  collective_material)
            print()
        return internal_wrapper
    return wrapper


def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print(
                '<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
        return internal_wrapper
    return wrapper


@big_container('plain cardboard')
@warehouse_decorator('bubble foil')
def pack_books(*args):
    print("We'll pack books:", args)


@big_container('colourful cardboard')
@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@big_container('strong cardboard')
@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


# pack_books('Alice in Wonderland', 'Winnie the Pooh')
# pack_toys('doll', 'car')
# pack_fruits('plum', 'pear')


class DecoratorExample:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("The decorator example from class")
        self.function(*args, **kwds)
        print("End of decorator")


class DecoratorWithArgs:

    def __init__(self, name) -> None:
        self.name = name

    def __call__(self, function) -> Any:

        def wrapper(*args, **kwrgs):
            print(f"The wrapper function arg is name = {self.name}")
            function(*args, **kwrgs)
            print("End of wrappers")
        return wrapper


@DecoratorExample
def simple_func(sentence):
    print(f"I am saying: {sentence}")


@DecoratorWithArgs(name="Decorator")
def simple_func_1(sentence):
    print(f"I am saying: {sentence}")


# a   = DecoratorExample("klaus")()
# print(a)
simple_func("Hello Word")
print("-"*15)
simple_func_1("Hello Word")
