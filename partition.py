def partition(arr):
	pivot = arr[0]

	j = 0
	for i in range(1, len(arr)):
		if arr[i] <= pivot:
			j += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[j], arr[0] = arr[0], arr[j]
	return arr


arr = [20, 7, 5, 3, 12, 7, 19, 2, 21]
arr = partition(arr)
print(arr)
