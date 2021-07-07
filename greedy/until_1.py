# 2. Greedy - Until 1 Problem

# Constraint
# 1. time limit 2 sec
# 2. input: 1 <= n <= 100000, 2 <= k <= 100000 (natural number)

# justification analysis source: 1 <= n and 2 <= k

# My Solution

n, k = map(int, input().split())
cnt = 0

while (n != 1):
  if n % k == 0:
    n //= k
    cnt += 1
    continue
  n -= 1
  cnt += 1

print(cnt)

# Reference - Technique Solution (T.C => log)
# n, k = map(int, input().split())

# result = 0
# while True:

# Subtract until n is the number of drops divided by k
#   target = (n // k) * k
#   result += (n - target)
#   n = target

# Escape a loop statement when n is less than k
# (when it is no longer divisible)
#   if n < k:
#     break

# Divide by k
#   result += 1
#   n //= k

# Subtract 1 for the last remaining number
# result += (n - 1)
# print(result)