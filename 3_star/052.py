N = int(input())

ans = 1
for i in range(N):
  A = list(map(int, input().split()))
  ans *= sum(A)

print(ans % (10**9+7))