N, K = input().split()
K = int(K)

for _ in range(K):
  ten = int(N, 8)

  if ten == 0:
    N = "0"
    continue

  nine = []
  while ten != 0:
    d = ten % 9
    nine.append('5' if d == 8 else str(d))
    ten //= 9

  N = ''.join(reversed(nine))

print(N)