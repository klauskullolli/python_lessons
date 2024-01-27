
INPUT_FIME = "number.txt"
OUT_FILE = "armstrong.txt"


def read_data(file: str):
    num = []
    try:
        with open(file, "+r") as f:
            # this is called list conprehantion in python
            num = [int(x) for x in f.read().split()]
            # print(num)
            f.close()
            print(num)
        return num

    except Exception as e:
        print(f"Error: {e}")
        return num


def is_Armstrong(a: int):
    lis_digit = [int(c) for c in str(a)]
    l = len(lis_digit)
    sum = 0
    for i in lis_digit:
        sum += i**l
    return True if sum == a else False



def solve_armstong():
    nums = read_data(INPUT_FIME)
    with open(OUT_FILE, "w") as f:
        nums =  [str(x) for x in nums if is_Armstrong(x)]
        # num = list(filter(lambda x : is_Armstrong(x), nums))
        print(nums)
        f.write("\n".join(nums))
        
    pass


if __name__ == "__main__":
    solve_armstong()
    # is_Armstrong(23453)
