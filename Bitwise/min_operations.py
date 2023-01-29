"""
Given two numbers a and b. In one operation you can pick any non negative integer x and either of a or b.
Now if you picked a then replace a with a&x else if you picked b then replace b with b&x.
Return the minimum number of operation required to make a and b equal.
Note: Here & represents bitwise AND operation.
"""

a = 5
b = 12

if a == b:
  print(0)
if a&b == a or a&b == b:
  print(1)
else:
  print(2)
