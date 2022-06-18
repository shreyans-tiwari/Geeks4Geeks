# arr = [11, 22, 33, 44, 55]
# k = 445
arr = [1, 2, 3, 4, 5]
k = 4

lo = 0
hi = len(arr) - 1

while lo < hi:
    mid = (lo + hi) // 2
    if k > arr[mid]:
        lo = mid+1
    elif k == arr[mid]:
        print(mid)
        break
    else:
        hi = mid - 1

print(-1)
