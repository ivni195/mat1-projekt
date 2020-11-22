#! /usr/bin/python3


# We use mod division for computation of the gcd(a, b).
def gcd_optimized(a, b):
    while b != 0:
        a, b = b, a % b

    # Returns gcd(a, b).
    return a


# rho-Pollard algorithm.
def rho_pollard_factorize(n, param):
    # Polynomial function modulo n used to generate a pseudorandom sequence.
    def f(x):
        return (x * x + 1) % n

    x = y = param
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd_optimized(abs(x - y), n)

    # If the algorithm fails, try again with a different parameter.
    if d == n:
        print(f'Algorithm failed. Retrying with parameter {param + 1}.')
        return rho_pollard_factorize(n, param + 1)
    else:
        return d


def main():
    a = 8051
    print(f'Rho-Pollard factor of {a}: {rho_pollard_factorize(a, 2)}')


if __name__ == '__main__':
    main()
