import heapq

def max_heap_sort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h, -value)
  for _ in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = max_heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)