H, W = map(int, input().split())
A = []
col_sums = [0] * H
row_sums = [0] * W

for h in range(H):
  A.append(list(map(int, input().split())))
  col_sums[h] = sum(A[h])
  for w in range(W):
    row_sums[w] += A[h][w]

for h in range(H):
  lines = []
  for w in range(W):
    lines.append(col_sums[h] + row_sums[w] - A[h][w])
  print(*lines)

