N, Q = map(int, input().split())
A = list(map(int, input().split()))

index = [i for i in range(N)]
out = []
offset = 0

for i in range(Q):
  T, x, y = map(int, input().split())
  x -= 1
  y -= 1
  if T == 1:
    t = A[(x-offset)%N]
    A[(x-offset)%N] = A[(y-offset)%N]
    A[(y-offset)%N] = t
  elif T == 2:
    offset = (offset+1) % N
  else:
    out.append(A[(x-offset)%N])

print(*out, sep='\n')