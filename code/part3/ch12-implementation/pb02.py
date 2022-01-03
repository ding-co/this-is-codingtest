input_data = input()

alpha_list, num_list = [], []

for ch in input_data:
  if ch.isalpha():
    alpha_list.append(ch)
  else:
    num_list.append(ch)

sum_num = sum(list(map(int, num_list)))

print(''.join(sorted(alpha_list)) + str(sum_num))

# Other Solution
# data = input()

# alpha_list = []
# sum_num = 0

# for ch in data:
#   if ch.isalpha():
#     alpha_list.append(ch)
#   else:
#     sum_num += int(ch)

# alpha_list.sort()

# if sum_num != 0:
#   alpha_list.append(str(sum_num))

# print(''.join(alpha_list))