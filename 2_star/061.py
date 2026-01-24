Q = int(input())

Answer = []
deck = []

for i in range(Q):
  t, x = map(int, input().split())
  if t == 1:
    deck.insert(0,x)
  elif t == 2:
    deck.append(x)
  else:
    Answer.append(deck[x-1])

print(*Answer, sep='\n')