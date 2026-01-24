N = int(input())

if N % 2 == 1:
  print()
  exit()

out = []

for i in range(2**N):
  string = ''
  cnt = 0
  for j in range(N):
    if i >> j & 1:
      string = ')' + string
      cnt += 1
    else:
      string = '(' + string
      cnt -= 1
    if cnt <0:
      break
  if cnt == 0:
    out.append(string)

print(*out, sep='\n')