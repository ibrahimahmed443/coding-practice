def merge_sorted_arrays(arr1, arr2):
       
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


arr1 = [1, 4, 10, 15, 20, 34]
arr2 = [5, 7, 11, 15]

merged = merge_sorted_arrays(arr1, arr2)
print(merged)
