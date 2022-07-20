"""
Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from
that element. Find the minimum number of jumps to reach the end of the array (starting from the first element).
If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.
"""
class Solution:
    def minJumps(self, arr, n):
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        if arr[0] >= n-1:
            return 1
        jump, currStart = 0, 1
        currEnd = currMaxReach = arr[0]
        
        while currStart < n-1:
            currMaxReach = max(currMaxReach, currStart+arr[currStart])
            if currMaxReach >= n-1:
                jump += 1
                break
            if currStart == currEnd:
                if currEnd == currMaxReach:
                    return -1
                jump += 1
                currEnd = currMaxReach
            currStart += 1
        
        return jump+1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
# } Driver Code Ends