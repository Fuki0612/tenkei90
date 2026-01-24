N = int(input())
A, B, C = map(int, input().split())

ans = 9999
for a in range(min(9999,N//A+1)):
  for b in range(min(9999-a,(N-a*A)//B+1)):
    r = N - a*A - b*B
    if r < 0 : break
    if r % C == 0:
      ans = min(ans,(a+b+(r // C)))

print(ans)