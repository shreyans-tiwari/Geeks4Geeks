"""
You are given N elements, you can remove any two elements from the list, note their sum, and
add the sum to the list. Repeat these steps while there is more than a single element in the list.
The task is to minimize the sum of these chosen sums.
"""

N = 5
arr = [1, 3, 7, 5, 6]

heapq.heapify(arr)
s = 0
       
while len(arr) > 1:
  t = 0
  t += heapq.heappop(arr)
  t += heapq.heappop(arr)
           
  heapq.heappush(arr, t)
  s += t
           
print(s)
