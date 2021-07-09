# 3. Implementation(Simulation & Brute Force) - The Royal Knight Problem

# Constraint
# 1. time limit: 1 sec
# 2. 8 X 8 coordinate plane
# 3. input: knight current position ex) a1 (column-row)

curr_pos = input()

# row
x = int(curr_pos[1])

# column
y = int(ord(curr_pos[0])) - int(ord('a')) + 1

steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (1, 2), (1, -2), (-1, -2)]

count = 0

for step in steps:
  nx = x + step[0]
  ny = y + step[1]

  if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
    count += 1

print(count)