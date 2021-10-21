A = [6,3,2,4,5,2,3,6,1]
n = len(A)

def selection_sort(A, n):
    for i in range(n):
        m = i
        for j in range(i, n):
            if A[j] < A[m]:
                m = j
        A[i], A[m] = A[m], A[i]


print(A)
selection_sort(A, n)
print(A)
