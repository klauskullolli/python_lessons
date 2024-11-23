import math


def is_palindrome(s):
    return s == s[::-1]


def biggest_palindrome(s):
    biggest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i : j + 1]) and len(s[i : j + 1]) > len(biggest):
                biggest = s[i : j + 1]
    return biggest


def factorial(n):
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    return prod


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# example a = 3, m = 11  a * x = 1 mod m
# using extended euclidean algorithm
# ax + my = 1
#
def extended_gcd(a, b):
    while a > 0 and b > 1:
        b, a = a, b % a
    return b

def modulus_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    while a > 0:
        m, a = a, m % a
    return m
    # return pow(a, -1, m)
    # or
    # ceil = math.ceil(m)
    # for i in range(1, m):
    #     if (a * i) % m == 1:
    #         return i
    # return None


def percentage_of_palindrome(s):
    s = list(s)
    letters_count = {}
    for i in s:
        count = letters_count.get(i)
        if count:
            letters_count[i] += 1
        else:
            letters_count[i] = 1
    Q = factorial(len(s))
    b_pal = list(biggest_palindrome(s))
    P = 1
    for i in b_pal:
        c = letters_count[i]
        P *= c
        letters_count[i] -= 1
    gcd_ = gcd(P, Q)
    return P // gcd_, Q // gcd_


def main():
    # a = 5
    # m = 1000007
    # print(modulus_inverse(a, m))
    # s = "caba"
    # print(percentage_of_palindrome(s))
    print(extended_gcd(3, 13))

    pass


if __name__ == "__main__":
    main()
