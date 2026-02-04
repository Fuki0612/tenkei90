H, W = map(int, input().split())

A = []
B = []
for _ in range(H):
  A.append(list(map(int, input().split())))
for _ in range(H):
  B.append(list(map(int, input().split())))

buttons = [[0] * W for _ in range(H)]
total = 0
for h in range(H):
  for w in range(W):
    if h == 0:
      if w == 0:
        buttons[h][w] = B[h][w] - A[h][w]
        total += abs(buttons[h][w])
      else:
        buttons[h][w] = B[h][w] - A[h][w] - buttons[h][w-1] 
        total += abs(buttons[h][w])
    elif h != H-1:
      if w == 0:
        buttons[h][w] = B[h][w] - A[h][w] - buttons[h-1][w]
        total += abs(buttons[h][w])
      else:
        buttons[h][w] = B[h][w] - A[h][w] - buttons[h][w-1] - buttons[h-1][w] - buttons[h-1][w-1]  
        total += abs(buttons[h][w])
    else:
      if w == 0:
        A[h][w] += buttons[h-1][w]
      else:
        A[h][w] += buttons[h-1][w-1] + buttons[h-1][w]

if A[H-1] == B[H-1]:
  print('Yes')
  print(total)
else:
  print('No')