import numpy as np

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

ans = []
for i in range(Q):
  E = int(input())
  y = -L/2 * np.sin(2 * E * np.pi / T)
  z = -L/2 * np.cos(2 * E * np.pi / T) + L/2
  D = np.sqrt((X)**2 + (y-Y)**2)
  theta = np.arctan(z / D) * 180 / np.pi
  print(theta)