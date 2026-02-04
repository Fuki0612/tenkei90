N, Q = map(int, input().split())

A = list(map(int, input().split()))
D = []

for i in range(1,N):
  D.append(A[i]-A[i-1])

total = sum([abs(x) for x in  D])
for j in range(Q):
  l, r, v = map(int, input().split())
  if 1 < l:
    total -= abs(D[l-2])
    D[l-2] += v
    total += abs(D[l-2])
  if r < N:
    total -= abs(D[r-1])
    D[r-1] -= v
    total += abs(D[r-1])
  print(total)
    