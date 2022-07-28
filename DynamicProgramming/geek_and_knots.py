"""
Given two walls A, B with M, N hooks respectively. You are given K ropes.
You can connect one hook on wall A with another hook on wall B.
Find the number of different ways you can use all the K ropes.
Two ways that use the exact same set of hooks from wall A and wall B are considered to be same.
"""


class Solution:
    def knots(self, M, N, K):
        i = M - K + 1
        num1 = 1
        while i <= M:
            num1 *= i
            i += 1

        j = N - K + 1
        num2 = 1
        while j <= N:
            num2 *= j
            j += 1

        den = 1
        while K > 0:
            den *= K
            K -= 1

        res = ((num1 * num2) // (den * den)) % (10 ** 9 + 7)

        return res


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        M, N, K = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.knots(M, N, K))
# } Driver Code Ends