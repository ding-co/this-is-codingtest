# 3. Greedy - Multiply or Add Problem

# Constraint
# 1. time limit 1 set
# 2. input: number string, 1 <= len(number string) <= 20

# My Solution

number_string = input()
result = int(number_string[0])

for number in number_string[1:]:
  if (result == 0) or (result == 1) or \
  (int(number) == 0 ) or (int(number) == 1):
    result += int(number)
    continue
  result *= int(number)

print(result)

# Reference Solution
# data = input()

# Replace the first character with a number and assign
# result = int(data[0])

# for i in range(1, len(data)):

# If either number is '0' or '1', do plus rather than multiply
#   num = int(data[i])
#   if num <= 1 or result <= 1:
#     result += num
#   else:
#     result *= num

# print(result)