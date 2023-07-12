"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""


""" Simple approach: """
# class Solution:
#     def twoSum(self, nums, target):
#    	    for i in range(0, len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]



""" Efficient approach: """

class Solution2:
    def twoSum(self, nums, target):
        map = {}
        for i in range(0, len(nums)):
            curr = nums[i]

            # curr + x = target
            x = target - curr

            if map.get(x) is not None:
                return [map.get(x), i]

            map[curr] = i

        return []
nums = [2,7,11,15]
target = 19

sol = Solution2()
print(sol.twoSum(nums, target))
