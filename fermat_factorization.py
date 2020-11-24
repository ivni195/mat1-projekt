#! /usr/bin/python3
import math


# Try to find factors of the form n=(a-b)(a+b) for an odd n.
def fermat_factorize(n):
    a = int(math.ceil(math.sqrt(n)))
    b2 = a * a - n
    # Look for a such that b = a^2 - n is a perfect square.
    while math.sqrt(b2) != math.floor(math.sqrt(b2)):
        a += 1
        b2 = a * a - n

    # Returns the smaller factor. Note that a-b is the biggest factor of n smaller that sqrt(n).
    # Thus, if the return value is equal to 1, then n is a prime.
    return a - int(math.sqrt(b2))


def main():
    a = 7
    b = 5959
    print(f'Factorize {a}: {fermat_factorize(a)}. Found factor is {fermat_factorize(a)} so {a} is prime.')
    print(f'Factorize {b}: {fermat_factorize(b)}. Found factor is {fermat_factorize(b)}.')


if __name__ == '__main__':
    main()
