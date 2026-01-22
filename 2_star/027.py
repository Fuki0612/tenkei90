N = int(input())

names = set()
days = []

for i in range(1,N+1):
  S = input()
  if S not in names:
    names.add(S)
    days.append(i)

print(*days, sep='\n')