# 4. Implementation - String reorder problem

# Constraint
# 1. time limit: 1 sec
# 2. input: 1 <= len(s) <= 10,000

# My Solution

input_s = input()

alpha_list = []
num_list = []

for s in input_s:
  if s.isalpha():
    alpha_list.append(s)
  else:
    num_list.append(int(s))

alpha_list.sort()
sort_alpha_list = "".join(alpha_list)

sum_num_list = str(sum(num_list)) if len(num_list) >= 1 else ""

print(sort_alpha_list + sum_num_list)