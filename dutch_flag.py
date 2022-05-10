def sort_array(A):
    pivot = 1
    start = mid = 0
    end = len(A) - 1

    while mid <= end:
        if A[mid] < pivot:
            p = A[mid]
            A[mid], A[start] = A[start], p #swap
            mid += 1
            start += 1
        elif A[mid] > pivot:
            p = A[mid]
            A[mid], A[end] = A[end], p #swap
            end -=1
        
        else : mid+=1
    return A

A = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
c = sort_array(A)
print(c)
    






