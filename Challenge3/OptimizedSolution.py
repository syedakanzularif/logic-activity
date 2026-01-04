def findMedianSortedArrays(a, b):
    if len(a) > len(b):
        a, b = b, a
    n, m = len(a), len(b)
    left, right = 0, n
    while left <= right:
        cutA = (left + right) // 2
        cutB = (n + m + 1) // 2 - cutA
        leftA  = float('-inf') if cutA == 0 else a[cutA - 1]
        rightA = float('inf')  if cutA == n else a[cutA]
        leftB  = float('-inf') if cutB == 0 else b[cutB - 1]
        rightB = float('inf')  if cutB == m else b[cutB]
        if leftA <= rightB and leftB <= rightA:
            if (n + m) % 2 == 0:
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            else:
                return float(max(leftA, leftB))
        elif leftA > rightB:
            right = cutA - 1
        else:
            left = cutA + 1
