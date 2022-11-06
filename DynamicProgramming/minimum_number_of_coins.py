"""
Given an infinite supply of each denomination of Indian currency
{ 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N.
Find the minimum number of coins and/or notes needed to make the change for Rs N.
You must return the list containing the value of coins required. 
"""

def minPartition(N):
        
    ans = []
        
    while N >= 2000:
        N -= 2000
        ans.append(2000)
        
    while N >= 500:
        N -= 500
        ans.append(500)
        
    while N >= 200:
        N -= 200
        ans.append(200)
        
    while N >= 100:
        N -= 100
        ans.append(100)
        
    while N >= 50:
        N -= 50
        ans.append(50)
        
    while N >= 20:
        N -= 20
        ans.append(20)
        
    while N >= 10:
        N -= 10
        ans.append(10)
        
    while N >= 5:
        N -= 5
        ans.append(5)
        
    while N >= 2:
        N -= 2
        ans.append(2)
        
    while N >= 1:
        N -= 1
        ans.append(1)
        
    return ans


print(minPartition(43))
