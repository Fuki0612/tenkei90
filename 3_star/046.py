INF = float('inf')

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

rA = [INF] * 46
rB = [INF] * 46
rC = [INF] * 46

for i in range(N):
  rA[A[i]%46] = 1 if rA[A[i]%46]==INF else rA[A[i]%46]+1 
  rB[B[i]%46] = 1 if rB[B[i]%46]==INF else rB[B[i]%46]+1
  rC[C[i]%46] = 1 if rC[C[i]%46]==INF else rC[C[i]%46]+1

ans = 0
for a in range(46):
  if rA[a] == INF:
    continue
  for b in range(46):
    if rB[b] == INF:
      continue
    for c in range(46):
      if rC[c] == INF:
        continue
      if (a+b+c)%46 == 0:
        ans += rA[a] * rB[b] * rC[c]

print(ans)