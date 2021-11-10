#Code to find out 2 large prime numbers, whitch can be used in RSA encryption. It is made of 3 function. First one will be used to establish if number is prime, second function will find a prime number inside a given and last function will output the product of the two primes.

def isPrime(n):
  for thing in range(2, n):
    if n % thing == 0:
      return False
  return True