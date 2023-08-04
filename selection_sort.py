def selection_sort(arr):
	n = len(arr)
	for i in range(0, n-1):
		min_index = i
		for j in range(i + 1, n):
			if arr[j] < arr[min_index]:
				min_index = j

		arr[i], arr[min_index] = arr[min_index], arr[i]

	return arr


arr = [5,1,0,2,10,4,3,1,3,2,9,11,8,15]
sorted_arr = selection_sort(arr)
print(sorted_arr)
