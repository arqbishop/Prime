# isprime
Short program that checks whether the given interger(s) is / are prime or not.

## How to use
- Make sure you have Python installed on your machine (Python 3.x).
- Place the program in the folder of your choice.
- Run your SHELL and move to the choosen folder.
- Type the command `py isprime.py [enter integer or integer sequence here]`.

## Why?
Prime numbers are interesting. [Their usage in cryptography](https://stackoverflow.com/questions/439870/why-are-primes-important-in-cryptography) even more.<br/>
Now, I personally just wanted to mess around with them... For example, using another short program `mkintergerseq.py` that creates a file `intergerseq` that contains an integer sequence up to a given number, I created a version of `integerseq` with integers from 0 to 999999 and used it to create `primenumbers0-999999`, a file containing all prime numbers from 0 to 999999 using the (very scary looking, I'll give you that) command `cat integerseq | xargs python3 isprime.py | grep -e "is prime" | cut -d " " -f 1 > primenumbers0-999999`.
<br/><br/>
What use will I make of it? No idea. Did I learn a lot while doing it? Yes, and it was quite fun as well... so I guess there's that.
