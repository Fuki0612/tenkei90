A, B, C = map(int, input().split())

def Euclidean(x,y):
  if x % y == 0:
    return y
  else :
    return Euclidean(y,x % y)

GCD = Euclidean(Euclidean(A,B),C)
print(A // GCD - 1 + B // GCD - 1 + C // GCD - 1 )