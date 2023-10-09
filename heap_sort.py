def build_heap(arr):
	for i in range(len(arr)//2 - 1, -1, -1):
		heapify_down(arr, len(arr), i)


def heapify_down(arr, size, index):
	left_child = index * 2 + 1
	right_child = index * 2 + 2
	
	largest = index
	if left_child < size and arr[left_child] > arr[largest]:
		largest = left_child

	if right_child < size and arr[right_child] > arr[largest]:
		largest = right_child

	if largest != index:
		#swap
		arr[index], arr[largest] = arr[largest], arr[index]
		heapify_down(arr, size, largest)


def heap_sort(arr):
	build_heap(arr)

	size = len(arr)
	for i in range(size - 1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify_down(arr, i, 0)


arr = [4,5,1,6,1,7,12,0,9, 3, 5]
heap_sort(arr)
print(arr)
