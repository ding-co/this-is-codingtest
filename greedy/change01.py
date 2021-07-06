# 1. Greedy - Change Problem

# N = 1260 (current money)

n = 1260
cnt = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  cnt = cnt + n // coin # cnt += n // coin
  n = n % coin          # n %= coin

print(cnt)