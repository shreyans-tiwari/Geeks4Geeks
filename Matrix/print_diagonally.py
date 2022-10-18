"""
Give a N * N square matrix A, return all the elements of its anti-diagonals from top to bottom.
"""


def downwardDigonal(N, A):
    # code here
    ans = []

    for k in range(N):
        i = 0
        j = k
        while j >= 0:
            ans.append(A[i][j])
            i += 1
            j -= 1

    for k in range(1, N):
        j = N - 1
        i = k
        while i < N:
            ans.append(A[i][j])
            i += 1
            j -= 1

    return ans


N = 3
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(downwardDigonal(N, A))
