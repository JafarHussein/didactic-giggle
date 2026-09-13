# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

nums = [4,5,6]
target = 10
sol_instance=Solution()
print(sol_instance.twoSum(nums, target))