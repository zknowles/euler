# sum of all primes below 2 million
import math
import sys

def isPrime(n):
    sqrtVal = int(math.ceil(math.sqrt(float(n))))
    if n % 2 == 0:
        return False
    for k in range(3, sqrtVal + 1, 2):
        if n % k == 0:
            return False

    return True

maxVal = int(sys.argv[1]) # feed in 2000000
sum_of_primes = 2 # 2 is a special case prime, start sum with this val

for k in range(3, maxVal, 2):
    if isPrime(k):
        sum_of_primes += k

print sum_of_primes
