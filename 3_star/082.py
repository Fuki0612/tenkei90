MAX = 10**9+7

L, R = map(int, input().split())

total = 0
len_r = len(str(R))
len_l = len(str(L))

if len_l == len_r :
  # print((L + R) * (R + 1 - L) * len_l // 2 % MAX)
  total += (L + R) * (R + 1 - L) * len_l // 2
  total %= MAX
else:
  for i in range(len_l,len_r+1):
    if i == len_l:
      left   = L
      right  = 10**i-1
    elif i == len_r:
      left   = 10**(i-1)
      right  = R
    else:
      left   = 10**(i-1)
      right  = 10**i-1
    # print((left + right) * (right + 1 - left) * i // 2 % MAX)
    total += (left + right) * (right + 1 - left) * i // 2
    total %= MAX

print(total % MAX)