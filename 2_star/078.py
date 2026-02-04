N, M = map(int, input().split())

d = [0] * (N+1)

for i in range(M):
  a, b = map(int, input().split())
  d[max(a,b)] += 1

ans = 0
for x in d:
  if x == 1:
    ans += 1
    
print(ans)