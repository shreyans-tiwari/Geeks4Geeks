"""
Given a number N. Find if it can be expressed as sum of two prime numbers.
"""

import math

m={i:1 for i in range(2,10**5+1)}

m[1]=0

for i in range(2,math.floor(math.sqrt(10**5))+1):
    if m[i]==1:
        j=2
        while(i*j<=10**5):
            m[i*j]=0
            j+=1


def isSumOfTwo (N):

    for i in range(1,N):
        if m[i]==1 and m[N-i]==1:
            return 'Yes'

    return 'No'


print(isSumOfTwo(34))
