# 선택 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

n = len(array)
for i in range(n):
  smallest_idx = i
  for j in range(i + 1, n):
    if array[smallest_idx] > array[j]:
      smallest_idx = j
  array[i], array[smallest_idx] = array[smallest_idx], array[i]

print(array)