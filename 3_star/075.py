from math import sqrt

def factorization(n):
  factors = []
  n1 = n
  for i in range(2, int(sqrt(n))+1):
    if n1 % i == 0:
      while n1 % i == 0:
        n1//=i
        factors.append(i)
      if n1 == 1:
        return factors
  if n1 != 1:
    factors.append(n1)
    return factors
  elif factors == []:
    return [n]

N = int(input())
primes = len(factorization(N))

count = 0
while primes > (2 ** count):
  count += 1

print(count)