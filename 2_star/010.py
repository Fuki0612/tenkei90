N = int(input())
CP = []
subset_A = [0]
subset_B = [0]

for i in range(N):
  C, P = map(int, input().split())
  if C == 1:
    subset_A.append(subset_A[-1] + P)
    subset_B.append(subset_B[-1])
  else :
    subset_A.append(subset_A[-1])
    subset_B.append(subset_B[-1] + P)    

Q = int(input())
ans = []

for i in range(Q):
  L, R = map(int, input().split())
  ans.append([subset_A[R]-subset_A[L-1], subset_B[R]-subset_B[L-1]])

for i in range(Q):
  print(*ans[i])