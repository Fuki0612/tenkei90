N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

out = 0
for i in range(N):
  out += abs(A[i] - B[i])
  
print(out)