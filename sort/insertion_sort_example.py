# Insertion sort example

def insertion_sort(array):
  for i in range(1, len(array)):
    for j in range(i, 1 - 1, -1):
      if array[j - 1] > array[j]:
        array[j - 1], array[j] = array[j], array[j - 1]
      else:
        break
  return array

input_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(insertion_sort(input_array))