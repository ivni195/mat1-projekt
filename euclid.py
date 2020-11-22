#! /usr/bin/python3

# Computes the greatest common divisor of the 2 given numbers.
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b

        else:
            b -= a

    # Returns gcd(a, b).
    return a


# We use mod division for computation.
def gcd_optimized(a, b):
    while b != 0:
        a, b = b, a % b

    # Returns gcd(a, b).
    return a

# Computes the GCD and solves GDC(a, b) = ax + yb for x, y.
def extended_euclid(a, b):
    old_r = a
    old_s = 1
    old_t = 0
    r = b
    s = 0
    t = 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - r * q
        old_s, s = s, old_s - s * q
        old_t, t = t, old_t - t * q

    # Returns gcd, x, y.
    return old_r, old_s, old_t

def main():
    print('gcd(1024 * 59, 1024 * 29) = ', gcd(1024 * 59, 1024 * 29))
    print('gcd(1024 * 59, 1024 * 29) = ', gcd_optimized(1024 * 59, 1024 * 29))
    gcd_, x ,y = extended_euclid(1432, 123211)
    print(f'gcd(1432, 123211) = {gcd_} = 1432 * {x} + 123211 * {y}')

if __name__ == '__main__':
    main()
