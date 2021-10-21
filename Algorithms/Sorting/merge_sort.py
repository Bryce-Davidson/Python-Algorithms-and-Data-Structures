A = [6,3,2,4,5,2,3,6,1]
n = len(A)

def merge_sort(A, n):
	if len(A) > 1:
		mid = n//2

		L = A[:mid]
		R = A[mid:]

		merge_sort(L, len(L))
		merge_sort(R, len(R))

		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				A[k] = L[i]
				i += 1
			else:
				A[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			A[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			A[k] = R[j]
			j += 1
			k += 1

print(A)
merge_sort(A, n)
print(A)
