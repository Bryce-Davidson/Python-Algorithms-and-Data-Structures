A = [6,3,2,4,5,2,3,6,1]
n = len(A)

def bubble_sort(A, n):
    for i in range(1, n):
        for j in range(n-i):
            if A[j+1] < A[j]:
                A[j], A[j+1] = A[j+1], A[j]

print(A)
bubble_sort(A, n)
print(A)
