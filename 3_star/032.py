import itertools

N = int(input())

A = []
for i in range(N):
  A.append(list(map(int, input().split())))

M = int(input())
romor = [[0] * (N+1) for _ in range(N+1) ]

for i in range(M):
  x, y = map(int, input().split())
  romor[x][y] = 1
  romor[y][x] = 1

score = float('inf')
for x in list(itertools.permutations([i for i in range(1,N+1)], N)):
  ans = 0
  flag = True
  for i in range(N-1):
    if romor[x[i]][x[i+1]] == 1:
      flag = False
      break
    ans += A[x[i]-1][i]
  if flag:
    ans += A[x[N-1]-1][N-1]
    score = min(ans,score)

if score == float('inf'):
  print(-1)
else:
  print(score)