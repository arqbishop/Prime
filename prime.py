import argparse

if __name__ == '__main__':

    # Argument creation
    parser = argparse.ArgumentParser(
        description = 'Checks whether a number is prime or not.'
    )

    parser.add_argument(
        'integer',
        metavar = 'integer',
        type = int,
        help = 'Enter the integer you wish to check whether it is prime or '
               'not.'
    )
    args = vars(parser.parse_args())

    # Variable creation according to the argument
    n = args['integer']

    if n <= 0 :
        raise ValueError('the integer must be greater than zero.')

    else:

        # Prime checking loop
        for i in range(2, n):
            if n % i == 0:
                print(n, 's equal to', i, '*', n // i, ': ', n, 'is not '
                                                                'a prime '
                                                                'number.')
                break

        else:
            print(n, 'is a prime number\n')
