N = int(input())
S = input()

ans = 0
L = 0
R = 0

while R != N:
  if S[L] == S[R]:
    R += 1
  else:
    ans += N - R
    L += 1

print(ans)