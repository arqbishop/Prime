from sys import argv

def is_str_integer(string):
    for char in string:
        if ord(char) < ord('0') or ord(char) > ord('9'):
            return False
    return True


def is_prime(n):
    if n == 0:
        return (False, "inf")
    if n == 1:
        return (False, 1)
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return (False, i)
    return (True, n)

    
if len(argv) > 1:
    cpt = 0
    for arg in argv[1:]:
        if is_str_integer(arg):
            n = int(arg)
            prime, div = is_prime(n)
            if prime:
                print(f"{n} is prime.")
            else:
                if div == "inf":
                    print(f"{n} has an infinite number of divisors : {n} is not prime.")
                elif div == 1:
                    print(f"{n} is only divisible by itself : {n} is not prime.")
                else:
                    print(f"{n} is equal to {div} * {n // div} : {n} is not prime.")
        else:
            cpt += 1
    if cpt == len(argv) - 1:  # The number of non-integer arguments is equal to the number of arguments
        print("None of the provided arguments were valid.")
else:
    print("You must provide at least one argument (integer) to the program.")
