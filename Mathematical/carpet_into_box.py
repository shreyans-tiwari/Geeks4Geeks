"""
There is a carpet of a size a*b [length * breadth]. You are given a box of size c*d.
The task is, one has to fit the carpet in the box in a minimum number of moves. 
In one move, you can either decrease the length or the breadth of the carpet by half (floor value of its half).
Note: One can even turn the carpet by 90 degrees any number of times, wont be counted as a move.
"""

A, B, C, D = 8, 13, 6, 10

moves1 = 0
l = A
b = B
while l > C:
  l = l // 2
  moves1 += 1
while b > D:
  b = b // 2
  moves1 += 1
        
l = A
b = B
moves2 = 0
while l > D:
  l = l // 2
  moves2 += 1
while b > C:
  b = b // 2
  moves2 += 1
        
print(min(moves1, moves2))
