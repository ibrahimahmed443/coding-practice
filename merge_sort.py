def merge(arr1, arr2):
       
    m = len(arr1)
    n = len(arr2)
    merged = []
    pointer1 = 0
    pointer2 = 0


    while pointer1 < m and pointer2 < n:
        if arr1[pointer1] <= arr2[pointer2]:
            merged.append(arr1[pointer1])
            pointer1 += 1
        else:
            merged.append(arr2[pointer2])
            pointer2 += 1
   
    # push any remaining elements
    while pointer1 < m:
        merged.append(arr1[pointer1])
        pointer1 += 1

    while pointer2 < n:
        merged.append(arr2[pointer2])
        pointer2 += 1

    return merged


def merge_sort(arr):
	if (len(arr) == 1):
		return arr

	mid = len(arr) // 2
	arr1 = merge_sort(arr[0: mid])
	arr2 = merge_sort(arr[mid:])
	merged = merge(arr1, arr2)
	return merged


arr = [3, 5, 1, 8, 1, 0, 9, 1, 7]
sorted = merge_sort(arr)
print(sorted)
