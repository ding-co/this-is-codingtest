# 2. Implementation(Brute Forcing) - Time Problem

# Constraint
# 1. time limit: 2 sec
# 2. input: 0 <= N <= 23

n = int(input())
count = 0

for hour in range(0, n + 1):
  for minute in range(0, 59 + 1):
    for second in range(0, 59 + 1):
      if "3" in str(hour) + str(minute) + str(second):
        count += 1

print(count)

# Reference: Other Person Solution Modify

# n = int(input())

# def other_solution(n):
#   count = 0

#   # Only focus on minute and second
#   hour = 6 * 10 * 6 * 10
#   exclude_3 = 5 * 9 * 5 * 9

#   # Check n
#   for i in range(0, n + 1):
#     if i == 3 or i == 13 or i == 23:
#       count += hour
#     else:
#       count += (hour - exclude_3)
  
#   return count

# print(other_solution(n))
