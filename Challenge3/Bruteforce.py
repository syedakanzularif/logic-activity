#BRUTE FORCE FOR CHALLNGE 3
def findMedianSortedArrays(a, b):
    n, m = len(a), len(b)
    total = n + m
    mid = total // 2
    i = j = 0
    prev = curr = 0
    for k in range(mid + 1):
        prev = curr
        if i < n and (j >= m or a[i] <= b[j]):
            curr = a[i]
            i += 1
        else:
            curr = b[j]
            j += 1
    if total % 2 == 0:
        return (prev + curr) / 2.0
    else:
        return float(curr)       
print(findMedianSortedArrays( [1, 3],  [2]))
