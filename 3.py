

def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A

print(insertion_sort([3,1,2,8,5,0,4])) 