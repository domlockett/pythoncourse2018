## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

## the level of complexity is described as how many (n)
## times does the worst case scenario have to call 
## an operation
## most worst case scenarios are n^2
def gcd(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    else: 
        r = x % y
    return gcd(y, r)

## Exercise 2
## Write a function using recursion that returns prime numbers less than 121
def find_primes(me = 121, primes = []):
    if me == 2:
        primes.append(2)
        return primes
    for x in range(2, me):
            if me % x == 0:
                break
    else:
        primes.append( me)
    return find_primes(me -1, primes)
                

