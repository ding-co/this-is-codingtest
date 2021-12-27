m, n = map(int, input().split())
move_array = [[0] * n for _ in range(m)]

x, y, direction = map(int, input().split())
move_array[x][y] = 1

whole_map = []
for i in range(m):
  whole_map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  if move_array[nx][ny] == 0 and whole_map[nx][ny] == 0:
    move_array[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if move_array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(count)