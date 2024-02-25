import itertools


def repeat(obj, time=None):
    if time is None:
        yield obj
    else:
        for i in range(time):
            yield obj


def repeat_default_inf(obj,  time: int = None):
    if time is None:
        while True:
            yield obj
    else:
        repeat(obj, time)


def itertool_example():
    # infinit iterator 
    counting = itertools.count(1, 2)
    ls = [next(counting) for _ in range(10)]
    print(ls)

    # finit iterator   
    it = range(12)
    print(f"it type: {type(it)}")

    # copy of iterator
    itNr = itertools.tee(it, 2)
    print(f"itNr element type: {type(itNr[0])}")
    for i in it:
        print(f"i {i}")
    for j in itNr[0]:
        print(f"j: {j}")

    ls_it = [it, *itNr]
    count = 0
    while True:
        if count >= 3:
            break
        try:
            print(next(ls_it[count]))
            pass
        except Exception as e:
            if isinstance(e, StopIteration):
                if count == 0:
                    print("it has stoped")
                else:
                    print(f"itNr[{count}] has stoped")
            else:
                if count == 0: 
                    print(f"Error at it: {e}, {type(e)}")
                else: 
                    print(f"Error at it: {e}, {type(e)}")
        finally:
            count += 1


def myFunc(*args: int):
    sum = 0
    for e in args:
        sum += e
    return sum


if __name__ == "__main__":

    itertool_example()
    # a = [1, 23, 4, 5]
    # b = [3, 4, 34, 3, 4]
    # c = [*a, *b]
    # print(c)

    pass
    # a = repeat(10)
    # b = repeat_default_inf(20)
    # print(type(b))
    # # c =  lambda x: (x+3, x+4, print("hello word"), x*2)
    # # print(c(4))
    # # print(type(c))
    # try:
    #     print(next(a))
    #     # print(next(a))
    #     for _ in range(10):
    #         print(next(b))
    # except Exception as e:
    #     if isinstance(e, StopIteration):
    #         print("End of iteration")
    #     else:
    # print(e)

    # a = [1, 2, 3, 4, 5, 6]
