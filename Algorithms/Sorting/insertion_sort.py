A = [1,3,2,4,5,2,3,6,1]
n = len(A)

def insertion_sort(A, n):
    for i in range(1, n):
        j = i
        # If the previous element to j is bigger than j
        while j > 0 and A[j] < A[j-1]:
            t = A[j]
            A[j] = A[j-1]
            A[j-1] = t
            j = j-1

print(A)
insertion_sort(A, n)
print(A)