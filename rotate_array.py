def rotate(nums, k):
    """
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    Do not return anything, modify nums in-place instead.
    """
    
    n = len(nums)
    k = k % n

    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)

def reverse(arr, start, end):
    if len(arr) <= 1:
        return

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)
print(nums)
