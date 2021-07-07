# 4. Greedy - Advanture Guild Problem

# Constraint
# 1. time limit 1 set
# 2. input: 1 <= n <= 100000 (adventurer number)
#    input: each adventurer's fear level <= n

n = int(input())
n_fear = list(map(int, input().split()))

# Total number of groups
group = 0

# The number of adventurers in the current group
count = 0

# Check the fear levels one by one (start with the low fear level)
for i in n_fear:

  # Include this adventurer in the current group
  count += 1

  # If the number of adventurers in the current group exceeds the current level of fear
  # grouping
  if count >= i:

    # Increase the total number of groups
    group += 1

    # Initialize the number of adventurers in the current group
    count = 0

# Print Total Number of Groups
print(group)