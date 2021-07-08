# 1. Implementation(Simulation) - Up Down Left Right Problem

# Constraint
# 0. Start Coordinate: (1,1), space: n X n square, ignore out of space
# 1. time limit: 2 sec
# 2. input: space size 1 <= n <= 100, move plan (U,D,L,R), 1 <= len(move) <= 100

# Get N input
n = int(input())
plans = input().split()

# Start Coordinate
x, y = 1, 1

# L, R, U, D => Move Direction
move_types = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# Check move plan one by one
for plan in plans:

  # Get after move Coordinate
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  # Ignore out of space
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  # Move Coordinate Update
  x, y = nx, ny

print(x, y)