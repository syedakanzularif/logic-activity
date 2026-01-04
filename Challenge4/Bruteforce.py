def kthSmallest(matrix, k):
    all_elements = []
    for row in matrix:
        for val in row:
            all_elements.append(val)   
    all_elements.sort()
    return all_elements[k - 1]
