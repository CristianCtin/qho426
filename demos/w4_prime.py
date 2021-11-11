#Code to find out 2 large prime numbers, whitch can be used in RSA encryption. It is made of 3 function. First one will be used to establish if number is prime, second function will find a prime number inside a given and last function will output the product of the two primes.

def isPrime(n):
  for thing in range(2, n):
    if n % thing == 0:
      return False
  return True

def findPrime(s, e):
  for i in range(s, e):
    if isPrime(i):
      return i

#print(findPrime(130440, 205454540))

def encrypt():
  x = int(input("Provide a starting point: "))
  y = int(input("Provide an endpoint: "))
  p1 = findPrime(x,y)
  x = int(input("Provide a starting point: "))
  y = int(input("Provide an endpoint: "))
  p2 = findPrime(x,y)
  return p1*p2

print(encrypt())