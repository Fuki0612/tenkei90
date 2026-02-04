import math

A, B = map(int, input().split())
gcd = math.gcd(A,B)

MAX = 10 ** 18
l = A//gcd*B
print('Large' if l>MAX else l)
