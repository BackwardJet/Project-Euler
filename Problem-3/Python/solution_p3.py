def largestPrimeFactor(num):
    largest_factor = 0
    for i in range(2,num):
        if (isPrime(i) and (num % i == 0)):
            largest_factor = i
    return largest_factor

def isPrime(n):
    # populates list with prime numbers from 2 to ceiling(sqrt(n))
    ceiling = int((n**0.5)+1)
    primes = [2]
    if (n % 2 == 0):
        return False
    iterator = 0
    for i in range(3,ceiling):
        j = 0
        while j < len(primes):
            if (i % primes[j] == 0):
                break
            j += 1            
        if j == len(primes):
            primes.append(i)
            iterator += 1
        if (n % primes[iterator] == 0):
            return False
    return True

assert(isPrime(3))
assert(not isPrime(14))
assert(not isPrime(64))
assert(not isPrime(2639))
assert(largestPrimeFactor(13195) == 29)


if __name__ == "__main__":
    print(largestPrimeFactor(600851475143))
    
