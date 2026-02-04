N = int(input())
A = list(map(int, input().split()))

SUM = sum(A)

if SUM % 10 != 0:
  print('No')
  exit()

A = A+A
goal = SUM // 10

bbnw = 0
l = 0
r = 0
while r < 2*N and r - l < N:
  if bbnw < goal:
    bbnw += A[r]
    r += 1
  elif bbnw == goal:
    print('Yes')
    exit()
  else:
    if l != r:
      bbnw -= A[l]
    l += 1
print('No')