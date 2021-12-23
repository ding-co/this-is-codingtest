input_data = input()
x = int(input_data[1])
y = ord(input_data[0]) - ord('a') + 1

steps = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, -2), (-1, 2), (1, 2), (1, -2)]

count = 0
for step in steps:
  nx = x + step[0]
  ny = y + step[1]

  if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
    count += 1

print(count)