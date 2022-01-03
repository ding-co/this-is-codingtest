n = input()

mid_idx = (len(n) // 2) - 1
left_sum = sum([int(n) for n in n[:mid_idx + 1]])
right_sum = sum([int(n) for n in n[mid_idx + 1:]])

if left_sum == right_sum:
  print("LUCKY")
else:
  print("READY")

# Other Solution
# n = input()
# n_len = len(n)
# n_sum = 0

# for i in range(n_len // 2):
#   n_sum += int(n[i])

# for i in range(n_len // 2, n_len):
#   n_sum -= int(n[i])

# if n_sum == 0:
#   print("LUCKY")
# else:
#   print("READY")