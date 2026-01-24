N = int(input())
A = list(list(map(int, input().split())))
A.sort()

Q = int(input())

out = []
for i in range(Q):
  B = int(input())
  
  L = 0
  R = N-1
  while R - L > 1:
    M = (L+R) // 2
    if B <= A[M]:
      R = M
    else:
      L = M

  out.append(min(abs(B-A[L]), abs(B-A[R])))

print(*out, sep='\n')