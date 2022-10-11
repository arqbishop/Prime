import os
import argparse

if __name__ == '__main__':

    # Argument creation
    parser = argparse.ArgumentParser(
        description = 'Checks whether a number is prime or not.'
    )

    parser.add_argument(
        'number',
        type = int,
        help = 'Enter the integer you wish to check whether it is prime or'
               'not.'
    )
    args = vars(parser.parse_args())

    # Variable creation according to the argument
    n = args['number']

    # Prime checking loop
    for i in range(2, n):
        if n % i == 0:
            print(n, "is equal to", i, "*", n // i, ": ", n, "is not a prime number.")
            break

    else:
        print(n, "is a prime number")
