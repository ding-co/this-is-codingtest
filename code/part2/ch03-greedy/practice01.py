n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_number = data[n - 1]
second_number = data[n - 2]

first_number_count = int(m / (k + 1)) * k
first_number_count += m % (k + 1)

result = 0
result += first_number * first_number_count
result += second_number * (m - first_number_count)

print(result)

# Reference Solution
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first_number = data[n - 1]
# second_number = data[n - 2]

# result = 0

# while True:
#   for _ in range(k):
#     if m == 0:
#       break
#     result += first_number
#     m -= 1
  
#   if m == 0:
#     break

#   result += second_number
#   m -= 1

# print(result)